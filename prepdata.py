# take in csv file, output data array

import csv
import pandas as pd
import numpy as np
import datetime
from sklearn.linear_model import LogisticRegression



high = "./vishruti_rudolph.csv"
low = "./olo_rudolph.csv"
highpitch = pd.read_csv(high)
highpitch = highpitch.loc[highpitch["Protocol"] == "L2CAP"]
lowpitch = pd.read_csv(low)
lowpitch = lowpitch.loc[lowpitch["Protocol"] == "L2CAP"]


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
    


#CHOOSE THE TIME STEP YOU WANT TO SEE FREQUENCIES
def get_freq(data, time_step_size):
    time_group = data['IntTimes'].apply(lambda x: x//time_step_size)
    data['group'] = time_group
    return data

#PERSON DATA CORRESPONDS TO
def add_person(data, person):
    data['Value'] = person
    return data

#GET NUMBER OF PACKETS/TIME STEP IN GET_FREQ
def freq_counts(data, person):
    counts = data.groupby(['group']).count()[['No.']]
    counts['Value'] = person
    return counts
    

#FOR CURRENT SET
high = timeseries_prep(highpitch, 1320, 1400)
high = add_person(high, 0)
low = timeseries_prep(lowpitch, 842, 907)
low = add_person(low, 1)
highgroup = get_freq(high, .1)
lowgroup = get_freq(low, .1)
highf = freq_counts(highgroup, 0)
lowf = freq_counts(lowgroup, 1)
alldata = pd.concat([high, low])
freqdata = pd.concat([highf, lowf])
lengthdata = alldata[['Length', 'Value']]
print(freqdata)
print(lengthdata)
