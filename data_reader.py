import numpy as np
import pandas as pa

# read the csv
path = "log.csv"
data = pa.read_csv(path)
# change Case IDs
case_ids = data['Case ID']
extracted_ids = {}
new_case_ids = []
counter = 0
for entry in case_ids:
    if entry not in extracted_ids.keys():
        extracted_ids[entry] = counter
        counter += 1
    new_case_ids.append(extracted_ids[entry])
data['Case ID'] = new_case_ids
print(data['Case ID'])