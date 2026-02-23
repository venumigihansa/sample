# Repair Proposal 21

- Incident: `inc-hotel-live-766c3d7968`
- Policy decision: `auto_apply`
- Risk tier: `tier0`
- Risk score: `14`

## Summary
Implement robust error handling and retry logic in the search_hotels_tool function to handle tool call failures and missing dependencies.

## Strategy
code_change

## Candidate Changes
### 1. `agent/tools.py` (update)
- Rationale: The tool call error indicates a failure in the invoked external tool. Adding retry logic and proper exception handling will prevent the service from crashing on transient failures and provide clearer error reporting.
- Suggested patch: diff --git a/agent/tools.py b/agent/tools.py
--- a/agent/tools.py
+++ b/agent/tools.py
@@ -1,9 +1,22 @@
-import requests
+import requests
+import time
+import logging
 
 
-def search_hotels_tool(query, location):
-    response = requests.get(f"https://api.hotel.com/search?q={query}&loc={location}")
-    response.raise_for_status()
-    return response.json()
+def search_hotels_tool(query, location, max_retries=3, backoff_factor=0.5):
+    for attempt in range(max_retries):
+        try:
+            response = requests.get(f"https://api.hotel.com/search?q={query}&loc={location}")
+            response.raise_for_status()
+            return response.json()
+        except Exception as e:
+            if attempt == max_retries - 1:
+                logging.error("search_hotels_tool failed after %d retries: %s", max_retries, e)
+                raise
+            else:
+                logging.warning("search_hotels_tool attempt %d failed: %s, retrying...", attempt+1, e)
+                time.sleep(backoff_factor * (2 ** attempt))
+

- Test updates: none

## Validation Plan
- Run integration tests for hotel-booking-agent under load to ensure search_hotels_tool succeeds.
- Inspect service logs for tool call errors; verify that retries are logged and failures are reported after max retries.
- Confirm that the service remains stable when the external hotel API is temporarily unavailable.

## Rollback Plan
- Revert the changes to agent/tools.py using the previous commit or by applying the inverse diff.

## Blast Radius
Limited to hotel-booking-agent service; does not affect other services.

## Confidence
0.9
