# Repair Proposal 26

- Incident: `inc-hotel-live-766c3d7968`
- Policy decision: `auto_apply`
- Risk tier: `tier0`
- Risk score: `29`

## Summary
Implement retry logic with exponential backoff for the hotel search tool to handle transient failures and broken search paths.

## Strategy
Wrap the search_hotels_tool function in a simple retry loop with exponential backoff to improve resilience against downstream failures.

## Candidate Changes
### 1. `agent/tools.py` (update)
- Rationale: The tool call error indicates transient failures; adding retry/backoff will allow the service to recover without immediate failure.
- Suggested patch: Replace search_hotels_tool implementation with a retry loop using exponential backoff.
- Content format: full_text
- Proposed content bytes: 1080
- Test updates: none

## Validation Plan
- Run unit tests for search_hotels_tool, simulating HTTP errors to verify retries.
- Deploy the updated agent/tools.py to a staging environment and trigger a failing hotel search request.
- Observe that the tool call succeeds after retries and that no unhandled exceptions are logged.
- Monitor production metrics for tool call error rate and latency after rollout.

## Rollback Plan
- Revert the changes in agent/tools.py to the previous version.
- Restart the hotel-booking-agent service to load the reverted code.

## Blast Radius
Low – only affects the hotel search functionality within the hotel-booking-agent service.

## Confidence
0.85
