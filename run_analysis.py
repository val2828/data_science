import data_reader as dr
import analyze_data as ad
import datetime as dt
import numpy as np
# specify run parameters
start_date = dt.datetime.strptime("2018/12/13 00:00:00", '%Y/%m/%d %H:%M:%S')
end_date = dt.datetime.strptime("2018/12/13 23:59:59", '%Y/%m/%d %H:%M:%S')

# run
dr.preprocess()
filtered_data = dr.filter_per_date(start_date,end_date, False)
#ad.get_stats_per_deployment(filtered_data)

