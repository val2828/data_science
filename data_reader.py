import numpy as np
import pandas as pa
import datetime as dt


# date change
def date_shift (date):
    date = date + dt.timedelta(days=1)
    return date.replace(hour = 0, minute = 0)
# getting the end date
def dep_finish (date_list):
    start_dates = date_list.tolist()
    start_dates.reverse()
    result = []
    for index in range(len(start_dates)):

        if (index + 1 < len(start_dates)):
            fin_date = start_dates[index + 1]
            fin_date = fin_date - dt.timedelta(days=1)
            fin_date = fin_date.replace(hour=23, minute= 59, second=0)
            result.append(fin_date)
        else:
            result.append(dt.datetime.today())
    result.reverse()
    return result
#read the csv
path = "log.csv"
data = pa.read_csv(path)
deployment_history = pa.read_csv('deployment_history.csv')

# change the timestamps into datetime objects
deployment_history['Deployed on'] = pa.to_datetime(deployment_history['Deployed on'], format='%Y-%m-%d %H:%M',errors='ignore')
deployment_history['Deployed on'] = deployment_history['Deployed on'].apply(func=date_shift)
deployment_history['Finished on'] = dep_finish(deployment_history['Deployed on'])


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
def filter_per_date(start_date, end_date, print_to_csv = False):

    ts_start_date = dt.datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
    ts_end_date = dt.datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S')

    filtered_data = data[(data['Start Timestamp'] > ts_start_date) & (data['Complete Timestamp'] < ts_end_date)]

    if (print_to_csv):
        path_to_data = 'filtered_logs/filtered_log' + start_date[0:10] + 'to' + end_date[0:10] + '.csv'
        filtered_data.to_csv(path_to_data)
    return filtered_data

def filter_per_deployment(deployments,print_to_csv = False):

    frames = []
    for deployment in deployments:
        ts_start_date = deployment_history.loc[deployment_history['Model'] == deployment, 'Deployed on'].iloc[0]
        ts_end_date = deployment_history.loc[deployment_history['Model'] == deployment, 'Finished on'].iloc[0]

        start_date = ts_start_date.strftime('%Y/%m/%d %H:%M:%S')
        end_date = ts_end_date.strftime('%Y/%m/%d %H:%M:%S')

        frames.append(filter_per_date(start_date,end_date,False))
    filtered_data = pa.concat(frames)
    if (print_to_csv):
        name_of_list = ''.join(deployments)
        path_to_data = 'filtered_logs/filtered_log' + name_of_list + '.csv'
        filtered_data.to_csv(path_to_data)
    return filtered_data




# assign de