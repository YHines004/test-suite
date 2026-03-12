# Armada Dev Validation Suite

## Purpose
Validate Armada scheduler functionality in the dev cluster.

## Tests Included

1. CPU Smoke Test
2. Gang Scheduling Test
3. Queue Priority Test
4. Failure Test
5. Lookout Observability Test

## Running Locally

./scripts/submit_tests.sh
python scripts/wait_for_completion.py
python scripts/check_results.py

## CI Execution

Triggered via GitHub Actions.

## Validation via Lookout

Search for jobSetId:

validation-suite

Verify job status and logs.