import data_reader as dr
import datetime as dt
import numpy as np
# specify run parameters
start_date = dt.datetime.strptime("2018/12/13 00:00:00", '%Y/%m/%d %H:%M:%S')
end_date = dt.datetime.strptime("2018/12/13 23:59:59", '%Y/%m/%d %H:%M:%S')

def get_stats_per_deployment(data):
    stats_summary_per_deployment = {}




    grouped_per_deployment = data.groupby(['Model'])
    for name, group  in grouped_per_deployment:
        dep_dict = {}
        dep_dict['Case count'] = group['Case ID'].nunique()
        stats_summary_per_deployment[name] = dep_dict

    print(stats_summary_per_deployment)
# add information to the data

# run

dr.preprocess()
filtered_data = dr.filter_per_date(start_date,end_date, True)

get_stats_per_deployment(filtered_data)

# stats per deployment

# stats per activity