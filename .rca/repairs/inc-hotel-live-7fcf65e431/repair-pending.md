# Applied Repair pending

- Incident: `inc-hotel-live-7fcf65e431`
- Base branch: `main`
- Summary: The search_hotels_tool fails when the configured hotel search path is missing or invalid, which is triggered by an injected bug mode. This patch adds a fallback path and validates the configured path, preventing the tool from crashing.
- Strategy: code_fix
- Confidence: 0.9

## Root Cause
The hotel-booking-agent service encountered an error while invoking a tool, likely due to a failing dependency or code issue.

## Changed Files
- `agent/app.py`
- `agent/tools.py`

## Why This Works
Aligns code behavior with diagnosed failure boundaries.

## Test Selection
- Strategy: `fallback_broad`
- Fallback triggered: `True`
- Fallback reason: `No Python tests discovered; running syntax-level Python verification.`
- Command: `python -m compileall -q .`

## Test Results
- Passed: `True`
- Failed count: `0`
- `python -m compileall -q .` -> exit `0`

## Rollback
- Revert repair branch commit and redeploy previous artifact if regressions are detected.
