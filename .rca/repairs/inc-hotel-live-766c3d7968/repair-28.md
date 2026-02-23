# Repair Proposal 28

- Incident: `inc-hotel-live-766c3d7968`
- Policy decision: `auto_apply`
- Risk tier: `tier0`
- Risk score: `14`

## Summary
Add defensive error handling and logging to the search_hotels_tool function to prevent tool call failures caused by broken hotel search paths.

## Strategy
Implement robust error handling and observability around the tool call to capture failures and provide fallback behavior.

## Candidate Changes
### 1. `agent/tools.py` (update)
- Rationale: The tool call fails due to unhandled exceptions when the hotel search path is broken. Adding try/except with detailed logging and a safe fallback prevents the failure from propagating and satisfies the recommended action to review the code symbol for bugs.
- Suggested patch: Wrap the search_hotels_tool implementation in try/except, log error details with thread_id and user_message, and return an empty list on failure.
- Content format: full_text
- Proposed content bytes: 800
- Test updates: none

## Validation Plan
- Run unit tests for search_hotels_tool, including a test that simulates a non‑200 HTTP response to verify the function logs the error and returns an empty list.
- Inspect logs from a staging deployment of hotel-booking-agent to confirm that tool call failures are captured with thread_id and user_message.
- Trigger a hotel search request in staging and ensure the service does not crash and returns a graceful fallback response.

## Rollback Plan
- Revert the changes in agent/tools.py to the previous version using git checkout or a previous commit.
- If any new logging configuration was added, remove it to restore the original state.

## Blast Radius
Low – only the search_hotels_tool function is modified; no other services are directly affected.

## Confidence
0.9
