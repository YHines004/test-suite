#!/bin/bash
set -e

JOBSET="validation-suite-$(date +%s)"

echo "Submitting Armada validation suite: $JOBSET"

for file in workloads/*.yaml; do
  echo "Submitting $file"
  armadactl submit $file --jobSetId $JOBSET
done

echo $JOBSET > jobset_id.txt