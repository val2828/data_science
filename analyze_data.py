import data_reader as dr
import datetime as dt
import numpy as np


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