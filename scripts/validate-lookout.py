import requests
import os
import sys

LOOKOUT_URL = os.environ["LOOKOUT_URL"]
JOBSET = open("jobset_id.txt").read().strip()
TOKEN = os.environ["ARMADA_TOKEN"]

url = f"{LOOKOUT_URL}/api/v1/jobs?jobSetId={JOBSET}"

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

print(f"Checking Lookout for jobset {JOBSET}")

resp = requests.get(url, headers=headers)

if resp.status_code != 200:
    print("Failed to query Lookout API")
    sys.exit(1)

jobs = resp.json()

if len(jobs) == 0:
    print("No jobs found in Lookout!")
    sys.exit(1)

print(f"Found {len(jobs)} jobs in Lookout")

for j in jobs:
    print(j["jobId"], j["state"])

print("Lookout validation PASSED")