# take in csv file, output data array
import csv
import pandas as pd
import numpy as np
import datetime

filename = "./vishruti_rudolph.csv"
bigdata = pd.read_csv(filename)
bigdata = bigdata.loc[bigdata["Protocol"] == "L2CAP"]

def convert_to_ts(timestr):
    x = datetime.datetime.strptime(timestr,'%M:%S.%f')
    time = x.minute*60+x.second+x.microsecond/1000000
    return time
#print(bigdata)


#CLEANS THE DATA
def timeseries_prep(bigdata, start_time, end_time):
    int_times = bigdata['Time'].apply(lambda x: convert_to_ts(x))
    bigdata['IntTimes'] = int_times
    smalldata = bigdata.loc[(bigdata['IntTimes'] >= start_time) & (bigdata['IntTimes'] <= end_time)]
    #print(smalldata)
    return smalldata
    

#FOR CURRENT SET
ya = timeseries_prep(bigdata, 1320, 1400)

#CHOOSE THE TIME STEP YOU WANT TO SEE FREQUENCIES
def get_freq(data, time_step_size):
    time_group = data['IntTimes'].apply(lambda x: x//time_step_size)
    data['group'] = time_group
    print(data.groupby(['group']).count())

get_freq(ya, .1)
