import time
import subprocess

JOBSET=open("jobset_id.txt").read().strip()

while True:
    out=subprocess.check_output(
        f"armadactl job-status --job-set {JOBSET}",
        shell=True
    ).decode()

    if "Running" not in out and "Queued" not in out:
        break

    print("Waiting for jobs to finish...")
    time.sleep(10)