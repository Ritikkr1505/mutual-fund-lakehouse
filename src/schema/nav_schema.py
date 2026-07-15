from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType,
    DoubleType,
    DateType
)

NAV_SCHEMA = StructType([
    StructField("scheme_code", IntegerType(), True),
    StructField("scheme_name", StringType(), True),
    StructField("fund_house", StringType(), True),
    StructField("category", StringType(), True),
    StructField("nav", DoubleType(), True),
    StructField("nav_date", DateType(), True)
])