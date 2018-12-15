import pandas as pa
import datetime as dt
import numpy as np
import metadata
import math


TASKS = metadata.TASKS
SKILLS = metadata.SKILLS

# Convert datetime into seconds
def dt_into_seconds(dt):
    result = dt.hour*3600 + dt.minute*60 + dt.second
    return result
# Convert seconds into datetime
def seconds_to_dt(seconds):
    hours = int(math.modf(seconds / 3600)[1])
    minutes = int(math.modf(seconds / 60)[1] - hours * 60)
    seconds = int(seconds - hours * 3600 - minutes * 60)
    result = dt.time(hour=hours,minute=minutes,second=seconds,microsecond=0)
    return result
# timedelta to seconds
def td_to_seconds(td):
    return td.total_seconds()


def get_stats_per_deployment(data):
    stats_summary_per_deployment = {}

    grouped_per_deployment = data.groupby(['Model'])
    for name, group  in grouped_per_deployment:
        dep_dict = {}
        dep_dict['Case count'] = group['Case ID'].nunique()
        stats_summary_per_deployment[name] = dep_dict

    print(stats_summary_per_deployment)
# add information to the data

# stats per deployment

# stats per activity

# get mean Cycle time per activity
def mean_cycle_times_per_activity(data):
    # service_times = {}
    # for task in TASKS.keys():
    #     service_times[task] = []
    data['Service Time'] = data['Complete Timestamp'] - data['Start Timestamp']

    data['Service Time'] = data['Service Time'].apply(td_to_seconds)
    # take all the activities in the data and find mean service times for them
    groupped_per_activity = data.groupby('Activity')
    mean_service_times_per_activity =groupped_per_activity['Service Time'].mean()
    mean_service_times_per_activity = mean_service_times_per_activity.apply(seconds_to_dt)


    # find waiting time for the activities. Waiting is the difference between start time of the activity and the end time of the previous activity.
    # those shall be per case. Then all the cases are aggregated into a single number. So we group everything by the case ID. Then we extract the numbers per case.
    # These records are added to the respective Dictionary, keeping track of the times per activity (we do  not need to remember
    # the information about eahc single case, just know the times)

    # combine them into cycle times. Probably return a tuple with mean time + variance