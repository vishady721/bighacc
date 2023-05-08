# take in csv file, output data array
import csv
import pandas as pd
import numpy as np

filename = "./vishruti_rudolph.csv"
bigdata = pd.read_csv(filename)
# bigdata = bigdata.loc[bigdata["Protocol"] == "A2DP"]

print(bigdata)

# this is how the spotify paper prepped their data
def timeseries_prep(bigdata, start_time, end_time, time_step_size):
    bigdata = bigdata[["Time", "Length"]]
    smalldata = bigdata.loc[(bigdata['Time'] >= start_time) & (bigdata['Time'] <= end_time)]
    roundedtimes = smalldata["Time"].apply(lambda x: int(x / time_step_size) * time_step_size)
    smalldata["Time"] = roundedtimes
    smalldata = smalldata.groupby(["Time"]).sum()
    # smalldata.to_csv(index=False, header=False)
    print(smalldata)
    
# not sure what the correct start and end times are
timeseries_prep(bigdata, 5000, 263993, 1)

