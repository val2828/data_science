import data_reader as dr
import analyze_data as ad
import metadata
import datetime as dt
import math

import numpy as np
# specify run parameters
TASKS = metadata.TASKS
SKILLS = metadata.SKILLS
start_date = "2018-12-11 00:00:00"
end_date = "2018-12-13 23:59:59"
deployments = ['Deployment_3.bpmn', 'Deployment_4.bpmn']

ts_start_date = dt.datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')


# prepare data
dr.preprocess()
# filter data
# filtered_data_per_deployment = dr.filter_per_deployment(deployments)
filtered_data_per_date = dr.filter_per_date(start_date,end_date)

# analyze
# ad.get_stats_per_deployment(filtered_data_per_date)
ad.mean_cycle_times_per_activity(filtered_data_per_date)
