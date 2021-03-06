import operator
import sensorfun
py_compile.compile(os.environ['pyduino']+'/python/post_processing/sensorfun.py')
import sensorfun
reload(sensorfun)
py_compile.compile(os.environ['pyduino']+'/python/post_processing/figlib.py')
import json
import figlib
import wafo.interpolate as wf
reload(figlib)
lw=5
ms=8
mew=3
grid_width=2
y_fontsize=20

with open('schedule.json') as f:
        schedule = json.load(f) #, object_pairs_hook=OrderedDict)
schedule['average_dry_density']=float(schedule['average_dry_density'])
schedule['specific_gravity']=float(schedule['specific_gravity'])
schedule['porosity']=1-schedule['average_dry_density']/schedule['specific_gravity']

sp_sch={}
plot_interpolate=False
#plot_interpolate=True
for line in open("schedule.ipt"):
    li=line.strip()
    if not li.startswith("#"):
        line_content=[x.strip() for x in li.split(',')]
        sch_name=line_content[2]
        sp_sch[sch_name]=pandas_scale.concat_data_roof(pd.datetime.strptime(line_content[0],'%Y/%b/%d %H:%M'),
            pd.datetime.strptime(line_content[1],'%Y/%b/%d %H:%M'),dt_s );
        sp_sch[sch_name].df.index=sp_sch[sch_name].df['date_time']

        sp_sch[sch_name].start_dt=pd.datetime.strptime(line_content[0],'%Y/%b/%d %H:%M')
        sp_sch[sch_name].end_dt=pd.datetime.strptime(line_content[1],'%Y/%b/%d %H:%M')

        sp_sch[sch_name].surface_area  =float(line_content[4])
        sp_sch[sch_name].merge_data(df=data.df, keys=['ec0']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data.df, keys=['tmp2']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data.df, keys=['pre1']   ,plot=plot_interpolate  ,coef=5e-15)  # done
        sp_sch[sch_name].merge_data(df=data.df, keys=['pre0']   ,plot=plot_interpolate  ,coef=5e-15)  # done
        sp_sch[sch_name].df['pre0']=(sp_sch[sch_name].df['pre0'].values-1005.35)*10.
        sp_sch[sch_name].df['pre1']=(sp_sch[sch_name].df['pre1'].values-1005.35)*10.

        time_start = np.datetime64('2018-02-27T08:00')
        time_end   = np.datetime64('2018-04-09T00:00')
        ##https://stackoverflow.com/questions/31617845/how-to-select-rows-in-a-dataframe-between-two-values-in-python-pandas/31617974
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df['tmp2'][mask]=np.random.random(len(mask))*50+710
        #sp_sch[sch_name].df.loc[mask,'tmp2']=np.random.random(len(mask))*50+710
        sp_sch[sch_name].df['ec2']=sp_sch[sch_name].df['tmp2']
#
        time_start=np.datetime64('2018-08-29T13:00')
        time_end=np.datetime64('2018-09-14T17:00')

        
        ## the new method has already considered the boundary effect
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tmp0']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tmp1']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tmp2']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tmp3']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tmp4']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tmp5']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tmp6']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tmp7']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tmp8']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tmp9']   ,plot=plot_interpolate  ,coef=5e-10)  # done


        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['su0']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['su1']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['su2']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['su3']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['su4']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['su5']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['su6']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['su7']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['su8']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['su9']   ,plot=plot_interpolate  ,coef=5e-10)  # done

        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo0']   ,plot=plot_interpolate  ,coef=5e-7)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo0']   ,plot=plot_interpolate  ,coef=5e-7)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo1']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo2']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo3']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo4']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo5']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo6']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo7']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo8']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo9']   ,plot=plot_interpolate  ,coef=5e-10)  # done



        time_start=np.datetime64('2018-08-29T13:00')
        time_end=np.datetime64('2018-09-14T17:00')
        mask_output=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        mask_input=data_mo_su.df['date_time'].between(time_start,time_end)
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo0']   ,plot=plot_interpolate  ,coef=5e-7,mask=mask_input) 
        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo0']   ,plot=plot_interpolate  ,coef=1e-16, start_time=time_start,end_time=time_end)
        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo1']   ,plot=plot_interpolate  ,coef=1e-16, start_time=time_start,end_time=time_end)
        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo2']   ,plot=plot_interpolate  ,coef=1e-16, start_time=time_start,end_time=time_end)
        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo3']   ,plot=plot_interpolate  ,coef=1e-16, start_time=time_start,end_time=time_end)
        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo4']   ,plot=plot_interpolate  ,coef=1e-16, start_time=time_start,end_time=time_end)
        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo5']   ,plot=plot_interpolate  ,coef=1e-16, start_time=time_start,end_time=time_end)
        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo6']   ,plot=plot_interpolate  ,coef=1e-16, start_time=time_start,end_time=time_end)
        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo7']   ,plot=plot_interpolate  ,coef=1e-16, start_time=time_start,end_time=time_end)
        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo8']   ,plot=plot_interpolate  ,coef=1e-16, start_time=time_start,end_time=time_end)
        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo9']   ,plot=plot_interpolate  ,coef=1e-16, start_time=time_start,end_time=time_end)
        #sp_sch[sch_name].merge_data2(df=data.df, keys=['ec0']   ,plot=plot_interpolate  ,coef=1e-16, start_time=time_start,end_time=time_end)
        #sp_sch[sch_name].merge_data2(df=data.df, keys=['ec2']   ,plot=plot_interpolate  ,coef=1e-16, start_time=time_start,end_time=time_end)

        sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['tc']  ,plot=plot_interpolate  ,coef=5e-08)  # done
        #sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['tp_box_7'],plot=plot_interpolate  ,coef=5e-12)  # done
        sp_sch[sch_name].df['tc'].loc[ sp_sch[sch_name].df['tc']<7  ]=np.nan
        #sp_sch[sch_name].df['tp_box_7'].loc[ sp_sch[sch_name].df['tp_box_7']<15 ]=np.nan

        # TO181205 soil sensor failed to work during 829 and 914, make evt zero. so air temperature was put in
        sp_sch[sch_name].df['tmp_soil_surf'] =  sp_sch[sch_name].df['tmp1'] 
        sp_sch[sch_name].df['tmp_soil_surf'].loc[mask_output]=  sp_sch[sch_name].df['tc'].loc[mask_output] 

        '''
        plt.figure()
        plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['tmp_soil_surf'])
        '''

        coef=-3.1 # been a while
        coef=-1.8 
        coef=-4.5 
        coef=-5.0 
        coef=-7.0 
        #coef=-2.1
        sp_sch[sch_name].df['mmo0']=(570.0**coef-sp_sch[sch_name].df['mo0']**coef)/(550.**coef-260**coef)*schedule['porosity']
        sp_sch[sch_name].df['mmo1']=(570.0**coef-sp_sch[sch_name].df['mo1']**coef)/(550.**coef-270**coef)*schedule['porosity']
        sp_sch[sch_name].df['mmo2']=(570.0**coef-sp_sch[sch_name].df['mo2']**coef)/(550.**coef-270**coef)*schedule['porosity']
        sp_sch[sch_name].df['mmo3']=(570.0**coef-sp_sch[sch_name].df['mo3']**coef)/(550.**coef-280**coef)*schedule['porosity']
        sp_sch[sch_name].df['mmo4']=(570.0**coef-sp_sch[sch_name].df['mo4']**coef)/(550.**coef-270**coef)*schedule['porosity']
        #sp_sch[sch_name].df['mmo4']=(570.0**coef-sp_sch[sch_name].df['mo4']**coef)/(550.**coef-285**coef)*schedule['porosity']
        sp_sch[sch_name].df['mmo5']=(570.0**coef-sp_sch[sch_name].df['mo5']**coef)/(550.**coef-270**coef)*schedule['porosity']
        #sp_sch[sch_name].df['mmo5']=(570.0**coef-sp_sch[sch_name].df['mo5']**coef)/(550.**coef-285**coef)*schedule['porosity']
        sp_sch[sch_name].df['mmo6']=(570.0**coef-sp_sch[sch_name].df['mo6']**coef)/(550.**coef-280**coef)*schedule['porosity']
        sp_sch[sch_name].df['mmo7']=(570.0**coef-sp_sch[sch_name].df['mo7']**coef)/(550.**coef-275**coef)*schedule['porosity']
        sp_sch[sch_name].df['mmo8']=(570.0**coef-sp_sch[sch_name].df['mo8']**coef)/(550.**coef-285**coef)*schedule['porosity']
        sp_sch[sch_name].df['mmo9']=(570.0**coef-sp_sch[sch_name].df['mo9']**coef)/(550.**coef-285**coef)*schedule['porosity']

        
        # this was in 20180522
        #sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['rainmm']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        
        # below was working in 20181023
        sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['dlyrainmm']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        sp_sch[sch_name].df['rainmm']= sp_sch[sch_name].df['dlyrainmm']
        time_start=np.datetime64('2018-04-20T10:00')
        time_end=np.datetime64('2018-04-20T23:59')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df.loc[mask,'rainmm']=np.linspace(0.93,18,np.sum(mask) )
        sp_sch[sch_name].df['rainmm'].loc[sp_sch[sch_name].df['rainmm']<0]=0
 
        # this is done because the sensors are made upside down later, also, some of the weather stations needs to make updates

        sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['ir_up']   ,plot=plot_interpolate  ,coef=5e-4,new_keys=['ir_up_daisy'])
        sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['ir_down']   ,plot=plot_interpolate  ,coef=5e-4,new_keys=['ir_down_daisy'])
        sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['ir_down']   ,plot=plot_interpolate  ,coef=5e-4,new_keys=['ir_up_camellia'])

        
        sp_sch[sch_name].df['ir_up_daisy'].loc[sp_sch[sch_name].df['ir_up_daisy']>19512]=np.nan
        sp_sch[sch_name].df['ir_up_daisy'].loc[sp_sch[sch_name].df['ir_up_daisy']<252]=252   # if it is given as np.nan, there will be breaking points
        sp_sch[sch_name].df['ir_up_camellia'].loc[sp_sch[sch_name].df['ir_up_camellia']<252]=252
        sp_sch[sch_name].df['ir_up_camellia'].loc[sp_sch[sch_name].df['ir_up_camellia']>19512]=np.nan
        # the correction here is to ensure camellia shows same value as daisy
        sp_sch[sch_name].df['ir_up_camellia_cor'] = (sp_sch[sch_name].df['ir_up_camellia']-252) *1.17+252
        # the script below uses early results from daisy while later results from camellia. 
        time_start=np.datetime64('2018-06-29T13:00')
        time_end=np.datetime64('2018-10-21T17:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df['ir_up_concat']=sp_sch[sch_name].df['ir_up_daisy']
        sp_sch[sch_name].df.loc[mask,'ir_up_concat']=      sp_sch[sch_name].df.loc[mask,'ir_up_camellia_cor']

        #plt.figure()
        #plt.plot(sp_sch[sch_name].df['date_time'],sp_sch[sch_name].df['ir_up_concat'])


        #mmo_surf is the surface moisture content, which is lateron used for surface resistance
        sp_sch[sch_name].df['mmo_surf']=sp_sch[sch_name].df['mmo0']

        #mmo0 starts to be exposed from 13 May
        time_start_mmo0=np.datetime64('2018-05-13T13:00')
        mask_mmo0=sp_sch[sch_name].df['date_time'].between(time_start_mmo0,sp_sch[sch_name].end_dt)
        sp_sch[sch_name].df.loc[mask_mmo0,'mmo0']=np.nan
        sp_sch[sch_name].df.loc[mask_mmo0,'tmp0']=np.nan

        #mmo1 starts to be exposed from 14 OCT
        time_start_mmo1=np.datetime64('2018-10-14T13:00')
        mask_mmo1=sp_sch[sch_name].df['date_time'].between(time_start_mmo1,sp_sch[sch_name].end_dt)
        sp_sch[sch_name].df.loc[mask_mmo1,'mmo1']=np.nan
        sp_sch[sch_name].df.loc[mask_mmo1,'tmp1']=np.nan


        mask_surf_mmo1=sp_sch[sch_name].df['date_time'].between(time_start_mmo0,time_start_mmo1)
        sp_sch[sch_name].df['mmo_surf'].loc[mask_surf_mmo1]= sp_sch[sch_name].df['mmo1'].loc[mask_surf_mmo1]

        mask_surf_mmo2=sp_sch[sch_name].df['date_time'].between(time_start_mmo1,sp_sch[sch_name].end_dt)
        sp_sch[sch_name].df['mmo_surf'].loc[mask_surf_mmo2]= sp_sch[sch_name].df['mmo2'].loc[mask_surf_mmo2]


        
        # this part was cancelled as the power is disabled. 
        time_start=np.datetime64('2018-08-29T13:00')
        time_end=np.datetime64('2018-09-14T17:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df.loc[mask,'tmp0']=np.nan
        sp_sch[sch_name].df.loc[mask,'tmp1']=np.nan
        sp_sch[sch_name].df.loc[mask,'tmp2']=np.nan
        sp_sch[sch_name].df.loc[mask,'tmp3']=np.nan
        sp_sch[sch_name].df.loc[mask,'tmp4']=np.nan
        sp_sch[sch_name].df.loc[mask,'tmp6']=np.nan
        sp_sch[sch_name].df.loc[mask,'tmp7']=np.nan
        sp_sch[sch_name].df.loc[mask,'tmp9']=np.nan

        #time_start=np.datetime64('2018-02-23T15:00')
        #time_end=np.datetime64('2018-03-02T15:00')
        #mask=data_weather_camellia.df['date_time'].between(time_start,time_end)
        #data_weather_camellia.df['rh_box_7'].loc[mask]=np.nan

        time_start=np.datetime64('2018-08-29T13:00')
        time_end=np.datetime64('2018-10-23T17:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df.loc[mask,'pre1']=np.nan

        # 100
        time_start=np.datetime64('2018-07-16T13:00')
        time_end=np.datetime64('2018-10-23T17:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df.loc[mask,'pre0']=np.nan

        sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['rh']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        sp_sch[sch_name].df['rh']*=0.01
        
        #TO181102 daisy humidity sensor was not working.....
        #sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['rh']   ,plot=plot_interpolate  ,coef=5e-08)  # done

        #sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['rh_box_7'],plot=plot_interpolate  ,coef=5e-12)  # done
        #time_start=np.datetime64('2018-01-27T15:00')
        #time_end=np.datetime64('2018-01-30T10:00')
        ##https://stackoverflow.com/questions/31617845/how-to-select-rows-in-a-dataframe-between-two-values-in-python-pandas/31617974
        #mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        #sp_sch[sch_name].df['rh'].loc[mask]=np.nan #time_start=np.datetime64('2018-02-24T15:00')
        #time_end=np.datetime64('2018-03-01T15:00')
        #mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        #sp_sch[sch_name].df['rh'].loc[mask]=np.nan


        #sp_sch[sch_name].df['rh_box_7'].loc[mask]=np.nan
        sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['wdspdkphavg2m']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        time_start=np.datetime64('2018-02-24T00:00')
        #sp_sch[sch_name].df['wdspdkphavg2m'].loc[mask]=np.nan
        sp_sch[sch_name].df['wdspdkphavg2m'].loc[ sp_sch[sch_name].df['wdspdkphavg2m']>12  ]=np.nan
        sp_sch[sch_name].df['wdspdkphavg2m'].loc[ sp_sch[sch_name].df['wdspdkphavg2m']<0  ]=np.nan

        sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['wdgstkph10m']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        sp_sch[sch_name].df['wdgstkph10m'].loc[ sp_sch[sch_name].df['wdgstkph10m']<0.  ]=np.nan

        #sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['wdspdkphavg2m']   ,plot=plot_interpolate  ,coef=5e-08)


        #plt.figure()
        #plt.plot(data_weather_daisy.df.index,data_weather_daisy.df['wdspdkphavg2m'] )

        #plt.figure()
        #plt.plot(data_weather_camellia.df.index,data_weather_camellia.df['wdspdkphavg2m'] )


        #plt.figure()
        #plt.plot(data_weather_camellia.df.index,data_weather_camellia.df['wdgstkph10m'] )
        sp_sch[sch_name].df['rh'].loc[ sp_sch[sch_name].df['rh']>100  ]=np.nan
        sp_sch[sch_name].df['rh'].loc[ sp_sch[sch_name].df['rh']<0  ]=np.nan




        time_start=np.datetime64('2018-02-03T15:00')
        time_end=np.datetime64('2018-02-05T15:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df['rh'].loc[mask]=np.nan

        time_start=np.datetime64('2018-03-02T15:00')
        time_end=np.datetime64('2018-03-10T15:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df['tmp7'].loc[mask]=np.nan
        sp_sch[sch_name].df['tmp6'].loc[mask]=np.nan
        sp_sch[sch_name].df['tmp9'].loc[mask]=np.nan



        #sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['tc']  ,plot=plot_interpolate  ,coef=5e-08)  # done


        #sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['p']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['p']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        sp_sch[sch_name].df['p'].iloc[sp_sch[sch_name].df['p'].values<100000]=np.nan
        sp_sch[sch_name].df['p'].iloc[sp_sch[sch_name].df['p'].values>150000]=np.nan


        time_start=np.datetime64('2018-04-20T00:00')
        time_end=np.datetime64('2018-04-25T15:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df['p'].loc[mask]=np.nan
        sp_sch[sch_name].df['tc'].loc[mask]=np.nan
        sp_sch[sch_name].df['wdspdkphavg2m'].loc[mask]=np.nan
        sp_sch[sch_name].df['wdgstkph10m'].loc[mask]=np.nan
        sp_sch[sch_name].df['rh'].loc[mask]=np.nan




        time_start=np.datetime64('2018-05-04T00:00')
        time_end=np.datetime64('2018-05-07T15:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df['p'].loc[mask]=np.nan
        sp_sch[sch_name].df['tc'].loc[mask]=np.nan
        sp_sch[sch_name].df['wdspdkphavg2m'].loc[mask]=np.nan
        sp_sch[sch_name].df['wdgstkph10m'].loc[mask]=np.nan
        sp_sch[sch_name].df['rh'].loc[mask]=np.nan


        time_start=np.datetime64('2018-05-29T00:00')
        time_end=np.datetime64('2018-05-31T15:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df['p'].loc[mask]=np.nan
        sp_sch[sch_name].df['tc'].loc[mask]=np.nan
        sp_sch[sch_name].df['wdspdkphavg2m'].loc[mask]=np.nan
        sp_sch[sch_name].df['wdgstkph10m'].loc[mask]=np.nan
        sp_sch[sch_name].df['rh'].loc[mask]=np.nan
        sp_sch[sch_name].df['rainmm'].loc[mask]=np.nan

        time_start=np.datetime64('2018-05-29T00:00')
        time_end=np.datetime64('2018-06-07T15:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df['ir_up_concat'].loc[mask]=np.nan
        
        


