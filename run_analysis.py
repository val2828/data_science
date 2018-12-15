import data_reader as dr
import analyze_data as ad
import datetime as dt
import numpy as np
# specify run parameters
start_date = "2018-12-11 00:00:00"
end_date = "2018-12-13 23:59:59"
deployments = ['Deployment_3.bpmn', 'Deployment_4.bpmn']

# run
dr.preprocess()
# dr.filter_per_deployment(deployments, True)
filtered_data = dr.filter_per_date(start_date,end_date, True)
# ad.get_stats_per_deployment(filtered_data)

