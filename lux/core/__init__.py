#  Copyright 2019-2020 The Lux Authors.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import pandas as pd
from .frame import LuxDataFrame
from .groupby import LuxDataFrameGroupBy, LuxSeriesGroupBy
from .series import LuxSeries
import cudf
#import config

global originalDF
# Keep variable scope of original pandas df
#originalDF = pd.core.frame.DataFrame
originalDF = cudf.DataFrame #.core.dataframe.
#originalSeries = pd.core.series.Series
originalSeries = cudf.Series #.core.series


def setOption(overridePandas=True):
#     dic = {'time' : ["2015-01-15 19:05:39"]}
#     cudf_df = cudf.DataFrame(dic)
#     print("type of cudf1: ", cudf_df)
    if overridePandas:
#         pd.DataFrame = (
#             pd.io.json._json.DataFrame
#         ) = (
#             pd.io.sql.DataFrame
#         ) = (
#             pd.io.excel.DataFrame
#         ) = (
#             pd.io.formats.DataFrame
#         ) = (
#             pd.io.sas.DataFrame
#         ) = (
#             pd.io.clipboards.DataFrame
#         ) = (
#             pd.io.common.DataFrame
#         ) = (
#             pd.io.feather_format.DataFrame
#         ) = (
#             pd.io.gbq.DataFrame
#         ) = (
#             pd.io.html.DataFrame
#         ) = (
#             pd.io.orc.DataFrame
#         ) = (
#             pd.io.parquet.DataFrame
#         ) = (
#             pd.io.pickle.DataFrame
#         ) = (
#             pd.io.pytables.DataFrame
#         ) = (
#             pd.io.spss.DataFrame
#         ) = (
#             pd.io.stata.DataFrame
#         ) = pd.io.api.DataFrame = pd.core.frame.DataFrame = pd._testing.DataFrame = LuxDataFrame
        cudf.DataFrame = cudf.core.dataframe.DataFrame = LuxDataFrame #cudf.core.dataframe.DataFrame
#         dic2 = {'time' : ["2017-01-15 19:05:39"]}
#         cudf_df2 = cudf.DataFrame(dic2)
#         print("type of cudf2: ", cudf_df2)
#         if pd.__version__ < "1.3.0":
#             pd.io.parsers.DataFrame = LuxDataFrame
#         else:
#             pd.io.parsers.readers.DataFrame = LuxDataFrame
        #pd.Series = pd.core.series.Series = pd.core.groupby.ops.Series = pd._testing.Series = LuxSeries
        cudf.Series = cudf.core.series.Series  = LuxSeries #cudf.core.series.Series
        #pd.core.groupby.generic.DataFrameGroupBy = LuxDataFrameGroupBy
        cudf.core.groupby.groupby.DataFrameGroupBy = LuxDataFrameGroupBy
        #pd.core.groupby.generic.SeriesGroupBy = LuxSeriesGroupBy
        cudf.core.groupby.groupby.SeriesGroupBy = LuxSeriesGroupBy
       
    else:
        #pd.DataFrame = pd.io.parsers.DataFrame = pd.core.frame.DataFrame = originalDF
        cudf.DataFrame  = originalDF #cudf.core.dataframe.DataFrame
        #pd.Series = originalSeries
        cudf.Series = originalSeries


setOption(overridePandas=True)
#print("init super2")
