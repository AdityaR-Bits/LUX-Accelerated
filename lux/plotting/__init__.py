# import pandas as pd
# import lux.core.frame as LF
# from lux.core.groupby import LuxDataFrameGroupBy, LuxSeriesGroupBy
# from lux.core.series import LuxSeries
# import cudf

# #import config

# # global originalDF
# # # Keep variable scope of original pandas df
# # #originalDF = pd.core.frame.DataFrame
# # originalDF = cudf.core.dataframe.DataFrame
# # #originalSeries = pd.core.series.Series
# # originalSeries = cudf.core.series.Series 


# def setOption(overridePandas=True):
#     if overridePandas:
# #         pd.DataFrame = (
# #             pd.io.json._json.DataFrame
# #         ) = (
# #             pd.io.sql.DataFrame
# #         ) = (
# #             pd.io.excel.DataFrame
# #         ) = (
# #             pd.io.formats.DataFrame
# #         ) = (
# #             pd.io.sas.DataFrame
# #         ) = (
# #             pd.io.clipboards.DataFrame
# #         ) = (
# #             pd.io.common.DataFrame
# #         ) = (
# #             pd.io.feather_format.DataFrame
# #         ) = (
# #             pd.io.gbq.DataFrame
# #         ) = (
# #             pd.io.html.DataFrame
# #         ) = (
# #             pd.io.orc.DataFrame
# #         ) = (
# #             pd.io.parquet.DataFrame
# #         ) = (
# #             pd.io.pickle.DataFrame
# #         ) = (
# #             pd.io.pytables.DataFrame
# #         ) = (
# #             pd.io.spss.DataFrame
# #         ) = (
# #             pd.io.stata.DataFrame
# #         ) = pd.io.api.DataFrame = pd.core.frame.DataFrame = pd._testing.DataFrame = LuxDataFrame
#         print("inside new init", type(cudf.DataFrame()))
#         LF.LuxDataFrame = cudf.DataFrame #= cudf.core.dataframe.DataFrame #cudf.core.dataframe.DataFrame
#         print("inside new init ldf", type(LF.LuxDataFrame()))
# #         if pd.__version__ < "1.3.0":
# #             pd.io.parsers.DataFrame = LuxDataFrame
# #         else:
# #             pd.io.parsers.readers.DataFrame = LuxDataFrame
#         #pd.Series = pd.core.series.Series = pd.core.groupby.ops.Series = pd._testing.Series = LuxSeries
        
#         LuxSeries = cudf.Series #= cudf.core.series.Series   #cudf.core.series.Series
#         #pd.core.groupby.generic.DataFrameGroupBy = LuxDataFrameGroupBy
#         LuxDataFrameGroupBy = cudf.core.groupby.groupby.DataFrameGroupBy 
#         #pd.core.groupby.generic.SeriesGroupBy = LuxSeriesGroupBy
#         LuxSeriesGroupBy = cudf.core.groupby.groupby.SeriesGroupBy 
       
#     # else:
#     #     #pd.DataFrame = pd.io.parsers.DataFrame = pd.core.frame.DataFrame = originalDF
#     #     cudf.DataFrame  = originalDF #cudf.core.dataframe.DataFrame
#     #     #pd.Series = originalSeries
#     #     cudf.Series = originalSeries


# setOption(overridePandas=True)
