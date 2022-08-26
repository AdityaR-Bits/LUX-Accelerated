import pandas as pd
import holoviews as hv
import numpy as np
import datetime
hv.extension('bokeh')
import re
import cudf
import time
import cupy
import numpy
from holoviews.operation.datashader import datashade,dynspread, rasterize,spread
from collections import Counter
import geopandas as gpd
import warnings
warnings.filterwarnings('ignore')



def plots(df,dat):
    
    pd.DataFrame(dat).to_csv("dummy.csv") 
    dat = pd.read_csv("dummy.csv")
    df = df.to_pandas2()
    print("pd type", type(dat))
    print("cd type", type(df))
    adder = False
    flag = False
    left_name="name"
    grph_num = 1
    for words in dat['collection']:
        lets = words.split("\n")
        for let in lets:
            res = re.findall(r'\w+', let)
            graph = res[-4]
            form = ""
            if graph =="histogram":
                starting = time.time()
                xlabel = res[3]
                ylabel = res[6]
                x = cudf.Series(df[xlabel])
                #x = LuxDataFrame(df[xlabel])
                x = cupy.fromDlpack(x.to_dlpack())
                frequencies, edges = cupy.histogram(x, bins=10)
                alpha = time.time()
                if len(frequencies)>10:
                    lis = list(zip(frequencies,edges))
                    lis.sort(key=lambda x:x[0],reverse=True)
                    lis=lis[:10]
                    frequencies, edges = zip(*lis)
                    frequencies = cupy.array(frequencies)
                    edges = cupy.array(frequencies)
                if abs(max(edges))>10000: form = '%.1e'
                curve=hv.Histogram((edges.get(), frequencies.get())).opts(axiswise=True,  xformatter=form, xlabel=xlabel, ylabel=ylabel, title = graph +" : "+str(grph_num), tools=["hover", ])#yformatter='%.1e',
                grph_num+=1
                if not adder: adder = curve
                else: adder+=curve
                print("time in histogram :", time.time() -starting)
            elif graph =="bar":
                starting = time.time()
                xlabel ="Records"
                ylabel = res[5]
                x=df.groupby(ylabel).count()
                x.reset_index(inplace=True) 
                lis = list(zip(x[ylabel].values_host, x.iloc[:, 1].values_host))
                if len(lis)>10: 
                    a=time.time()
                    lis.sort(key=lambda x:x[1],reverse=True)
                    lis=lis[:10]
                    print("========", time.time()-a)
                if abs(x.iloc[:, 1].max())>10000: form = '%.1e'
                curve = hv.Bars(lis).opts(invert_axes=True).opts(axiswise=True, xlabel=ylabel, ylabel =xlabel,xformatter=form, title = graph +" : "+str(grph_num), tools=["hover", ])
                grph_num+=1
                if not adder: adder = curve
                else: adder+=curve
                print("time in inverted bar :", time.time() -starting)
            elif graph =="line":
                starting = time.time()
                xlabel = res[2]
                factor = re.search(xlabel + '(.*)y', "".join(res)).group(1)
                ylabel = "Records"
                if factor == 'dayofweek':
                    x = cudf.DatetimeIndex(df[xlabel])
                    x = cudf.DataFrame(x.dayofweek, columns = ["date"])
                    x["count"] = x['date']
                elif factor =='month':
                    x = cudf.DatetimeIndex(df[xlabel])
                    x = cudf.DataFrame(x.month, columns = ["date"])
                    x["count"] = x['date']
                elif factor =="year":
                    x = cudf.DatetimeIndex(df[xlabel])
                    x = cudf.DataFrame(x.year, columns = ["date"])
                    x["count"] = x['date']
                else:
                    x = df.rename(columns={xlabel: "date"})
                    cols = df.columns
                    for c in cols: 
                        if c!='date':
                            extra_name=c
                            break
                    x = x[['date',extra_name]]
                    x = x.rename(columns={extra_name: "count"})

                x = x.groupby("date").count()
                x.reset_index(inplace=True)
                x = x.sort_values('date')
                x.reset_index(inplace=True)
                x.reset_index(inplace=True)
                #print(x)
                lis = list(zip(x['level_0'].values_host, x['count'].values_host)) if len(factor)==0 else list(zip(x['date'].values_host, x['count'].values_host))
                curve = rasterize(hv.Curve(lis)).opts(axiswise=True,yformatter='%.1e', xlabel=xlabel, ylabel=ylabel , title = graph +" : "+str(grph_num),tools=["hover", ])
                #curve = datashade(hv.Curve(lis, hv.Dimension(xlabel), "Number of " +ylabel)).opts(axiswise=True,yformatter='%.1e', xlabel=xlabel, ylabel=ylabel , title = graph +" : "+str(grph_num))
                grph_num+=1
                if adder==False: adder = curve
                else: adder+=curve
                print("time in linecurve :", time.time() -starting)
            elif graph == "scatter":
                starting = time.time()
                xlabel = res[2]
                ylabel = res[4]
                x = cudf.Series(df[xlabel])
                y = cudf.Series(df[ylabel])
                z = cudf.concat([x,y],axis=1)
                if abs(x.max())>10000: form = '%.1e'
                curve = rasterize(hv.Scatter(z)).opts(axiswise=True, xformatter = form, xlabel=xlabel, ylabel=ylabel, title = graph +" : "+str(grph_num), tools=["hover", ],cmap=['blue'])#,threshold=0.75)#yformatter='%.1e', 
                grph_num+=1
                if adder==False: adder = curve
                else: adder+=curve
                print("time in scatterplot :", time.time() -starting)
            # elif graph =="geographical":
            #     starting = time.time()
            #     geo = res[2]
            #     vals = res[5]
            #     x=df.groupby(geo).mean()
            #     x.reset_index(inplace=True)
            #     if not flag:
            #         if geo in ["states","state","States","State", "STATES", "STATE"]:
            #             geography = gpd.read_file("us-states.json")
            #             if isinstance(x[geo].iloc[0],numpy.int64):
            #                 left_name = "fips_num"
            #                 geography[left_name] = geography["id"].apply(lambda x: int(state_codes[x]))
            #             geography_pop = geography.merge(x.to_pandas(), left_on=left_name, right_on=geo)
            #         elif geo in ["Country", "COUNTRY", "country", "COUNTRIES","countries", "Countries"]:
            #             geography = gpd.read_file("countries.geojson")
            #             geography_pop = geography.merge(x.to_pandas(), left_on="ADMIN", right_on=geo)
            #         flag =True
            #     if geo in ["states","state","States","State", "STATES", "STATE"]:
            #         curve = rasterize(hv.Polygons(data=geography_pop, vdims=[vals, geo])).opts(axiswise=True, xlim=(-170, -60), ylim=(10,75),  height=300, width=400, title=vals+" : "+str(grph_num), tools=["hover", ])#, colorbar=True, colorbar_position="right"
            #     elif geo in ["Country", "COUNTRY", "country", "COUNTRIES","countries", "Countries"]:
            #         curve =  rasterize(hv.Polygons(data=geography_pop, vdims=[vals, geo]).opts(colorbar=True, colorbar_position="right")).opts(axiswise=True, height=300, width=400, title=vals+" : "+str(grph_num), tools=["hover", ])#, colorbar=True, colorbar_position="right"
            #     grph_num+=1
            #     if adder==False: adder = curve
            #     else: adder+=curve
            #     print("time in choropleth :", time.time() -starting)
    print("adder type;", type(adder))
    return adder