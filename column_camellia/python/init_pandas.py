#import sys
#sys.modules[__name__].__dict__.clear()
import os
import numpy as np
#http://stackoverflow.com/questions/5607283/how-can-i-manually-generate-a-pyc-file-from-a-py-file
import py_compile
import sys
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import pandas as pd
import pdb


################################get scale data####################################################################


dt_s=3600
scale=1
del scale
#os.path.dirname(os.path.realpath(__file__))

current_path=os.getcwd()
sys.path.append('/home/chenming/Dropbox/scripts/github/pyduino/python/post_processing/')
py_compile.compile('/home/chenming/Dropbox/scripts/github/pyduino/python/post_processing/pandas_scale.py')
py_compile.compile('/home/chenming/Dropbox/scripts/github/pyduino/python/post_processing/constants.py')

import pandas_scale
import constants
reload(pandas_scale)
reload(constants)


python_file_path=current_path+'/python/'
sys.path.append(python_file_path)
# change the date time header as datetime to make life easier
#data_list_data_roof=os.listdir(current_path+'/data/data_roof/')
data_file_path=current_path+'/sensor_data/'    # warning, all the files should be .dat

#data_header=['mo0','mo1','mo10','mo11','mo12','mo13','mo14','mo15','mo2','mo3','mo4','mo5','mo6','mo7','mo8',
#    'mo9','su1','su2','su3','su4','date_time','tp1','tp11','tp2','tp3','tp4','tp8d','tpa3','tpf0','tphr45','tphr47']

data_header=['evap','ip','mo0','mo1','mo10','mo11','mo12','mo13','mo14','mo15','mo2','mo3','mo4','mo5',
'mo6','mo7','mo8','mo9','t26_begin','t26_peak','t45_begin','t45_peak','t57_begin','t57_peak','t7b_begin'
,'t7b_peak','te2_begin','te2_peak','tfb_begin','tfb_peak','timestamp']

data_date_time=['timestamp']
# 09/03/2017 here x[:-5] only sorts out from start to -5 position
# one can check the correct by
# dateparse('2017-03-09T09:02:48.588Z')
# and see if the parsing is successful
#dateparse =  lambda x: pd.datetime.strptime(x[:-5], '%Y-%m-%dT%H:%M:%S')  # sparkfun output
# this new function is better as it provides miniseconds parsing as well. 
dateparse =  lambda x: pd.datetime.strptime(x[:-1], '%Y-%m-%dT%H:%M:%S.%f')  # sparkfun output

# 09/03/2017 remove the index column at the very beginning, by default, pandas will produce a column from first one.
index_col_sw=False

data=pandas_scale.pandas_scale(file_path=data_file_path,
    source='raw',
    sep=',',
    header=1,
    names=data_header,
    parse_dates=data_date_time,
    date_parser=dateparse,
    index_col=index_col_sw
    )

#
data.df.sort_values('timestamp',inplace=True)
### https://stackoverflow.com/questions/37787698/how-to-sort-pandas-dataframe-from-one-column
### reverse the dataframe by timestamp as the result is upside down
##data.df.sort_values('timestamp',inplace=True)
##
#data.df = data.df.reset_index(drop=True)
##
### 'date_time'  is the column with corrected time zones
data.df['date_time']=data.df['timestamp']+pd.to_timedelta(10, unit='h')
#
#
##data.save_as_csv (fn='data_merged.csv')
##data.save_as_hdf5(fn='data_merged.hd5')
#
#
####   special treatment
##data.df['mo_0'][data.df['mo_8']>570]=np.nan
##data.df['mo0'][data.df['mo0']>400]=np.nan
#data.df['mo1'][data.df['mo1']>400]=np.nan
#data.df['mo2'][data.df['mo2']>400]=np.nan
#data.df['mo3'][data.df['mo3']>400]=np.nan
#data.df['mo4'][data.df['mo4']>400]=np.nan
data.df['mo8'][data.df['mo8']<200]=np.nan
#data.df['mo4'][data.df['mo4']<150]=np.nan
#data.df['mo4'][:5000][data.df['mo4'][:5000]<200]=np.nan
#data.df['mo5'][data.df['mo5']>400]=np.nan
#data.df['mo6'][data.df['mo5']>400]=np.nan
#data.df['mo7'][data.df['mo7']>400]=np.nan
#
#
#data.df['mo1'] = (data.df['mo1']**0.5  -180.0**0.5)/(300.0**0.5-180.0**0.5)
#data.df['mo2'] = (data.df['mo2']**0.5  -150.0**0.5)/(300.0**0.5-150.0**0.5)
#data.df['mo3'] = (data.df['mo3']**0.5  -150.0**0.5)/(300.0**0.5-150.0**0.5)
#data.df['mo4'] = (data.df['mo4']**0.5  -150.0**0.5)/(300.0**0.5-150.0**0.5)
#data.df['mo5'] = (data.df['mo5']**0.5  -150.0**0.5)/(300.0**0.5-150.0**0.5)
#data.df['mo7'] = (data.df['mo7']**0.5  -150.0**0.5)/(300.0**0.5-150.0**0.5)
#data.df['mo10'] = (data.df['mo10']**0.5-150.0**0.5)/(280.0**0.5-150.0**0.5)
#
#
##data.df['mo_8'][data.df['mo_8']>570]=np.nan
#
##data.df['t_19_end'][data.df['t_19_end']>32]=np.nan
##data.df['t_19_begin'][data.df['t_19_begin']>32]=np.nan
##data.df['t_14_begin'][data.df['t_14_begin']>32]=np.nan
##data.df['t_19_end'][data.df['t_19_end']>32]=np.nan
##data.df['t_14_end'][data.df['t_14_end']>32]=np.nan


