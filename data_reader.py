import numpy as np
import pandas as pa
import datetime as dt


# date change
def date_shift (date):
    date = date + dt.timedelta(days=1)
    return date.replace(hour = 0, minute = 0)

#read the csv
path = "log.csv"
data = pa.read_csv(path)
deployment_history = pa.read_csv('deployment_history.csv')

# change the timestamps into datetime objects
deployment_history['Deployed on'] = pa.to_datetime(deployment_history['Deployed on'], format='%d-%m-%y %H:%M',errors='ignore')
deployment_history['Deployed on'] = deployment_history['Deployed on'].apply(func=date_shift)
data['Start Timestamp'] = pa.to_datetime(data['Start Timestamp'], format='%Y/%m/%d %H:%M',errors='ignore')
data['Complete Timestamp'] = pa.to_datetime(data['Complete Timestamp'], format='%Y/%m/%d %H:%M',errors='ignore')

# change Case IDs, add deployemnts and optionally create a csv output to the specialized folder
def preprocess(print_to_file=False):
    # assign new ids
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

    # add deployments
    deployments = []
    for timestamp in data['Complete Timestamp']:
        model = ''
        for dep_date in (deployment_history['Deployed on']):

            if (dep_date < timestamp):
                model = (deployment_history.loc[deployment_history['Deployed on'] == dep_date, "Model"].iloc[0])
                break
        deployments.append(model)

    data['Model'] = pa.Series(deployments)

    # filter per date
def filter_per_date(start_date, end_date, print_to_csv = True):
    filtered_data = data[(data['Start Timestamp'] > start_date) & (data['Complete Timestamp'] < end_date)]
    if (print_to_csv):
        filtered_data.to_csv('filtered_log.csv')
    return filtered_data




# assign de