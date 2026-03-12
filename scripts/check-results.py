import subprocess
import json
import sys

JOBSET=open("jobset_id.txt").read().strip()

cmd=f"armadactl job-status --job-set {JOBSET} --output json"

result=subprocess.check_output(cmd,shell=True)
jobs=json.loads(result)

failures=[]

for job in jobs:
    status=job["state"]
    jobid=job["jobId"]

    print(f"{jobid}: {status}")

    if jobid=="fail-test":
        if status!="FAILED":
            failures.append(jobid)
    else:
        if status!="SUCCEEDED":
            failures.append(jobid)

if failures:
    print("FAILED TESTS:",failures)
    sys.exit(1)

print("ALL TESTS PASSED")