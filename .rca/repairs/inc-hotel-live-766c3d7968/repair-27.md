# Repair Proposal 27

- Incident: `inc-hotel-live-766c3d7968`
- Policy decision: `auto_apply`
- Risk tier: `tier0`
- Risk score: `14`

## Summary
Wrap search_hotels_tool in a retry/backoff mechanism to handle transient tool failures.

## Strategy
Implement retry/backoff and circuit breaker patterns for tool calls.

## Candidate Changes
### 1. `agent/tools.py` (update)
- Rationale: The tool call error indicates a transient failure; adding retry/backoff will mitigate it.
- Suggested patch: Add retry/backoff wrapper around search_hotels_tool.
- Content format: full_text
- Proposed content bytes: 1895
- Test updates: Add test for search_hotels_tool retry behavior in tests/test_search_hotels_tool.py

## Validation Plan
- Run unit tests for agent/tools.py to ensure the function returns expected results.
- Execute the new test in tests/test_search_hotels_tool.py to verify retry logic works.
- Deploy to a staging environment and trigger a hotel search to confirm no tool_call_error events are emitted.
- Monitor production logs for any remaining tool_call_error events.

## Rollback Plan
- Revert the changes made to agent/tools.py to the previous version.
- Remove the added test file or revert its changes.

## Blast Radius
Low – only affects hotel search tool invocation within the hotel-booking-agent service.

## Confidence
0.85
