import data_reader as dr
# specify run parameters
start_date = "2018/11/29 00:00:00"
end_date = "2018/12/01 23:59:59"

# add information to the data

# run

dr.preprocess()
filtered_data = dr.filter_per_date(start_date,end_date)
