from pyspark.sql import DataFrame
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number


def duplicate_validation(df: DataFrame, primary_key: str):
    """
    Splits DataFrame into valid and duplicate records.

    Parameters
    ----------
    df : DataFrame
        Input dataframe

    primary_key : str
        Column used to detect duplicates

    Returns
    -------
    valid_df
        Records after removing duplicates

    duplicate_df
        Duplicate records
    """

    window = Window.partitionBy(primary_key).orderBy(primary_key)

    ranked_df = df.withColumn(
        "row_num",
        row_number().over(window)
    )

    valid_df = ranked_df.filter("row_num = 1").drop("row_num")

    duplicate_df = ranked_df.filter("row_num > 1").drop("row_num")

    return valid_df, duplicate_df