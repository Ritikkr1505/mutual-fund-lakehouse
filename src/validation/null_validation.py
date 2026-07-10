from functools import reduce
from pyspark.sql.functions import col


def null_validation(df, mandatory_columns):
    """
    Validate mandatory columns for NULL values.

    Parameters:
    ----------
    df : pyspark.sql.DataFrame
        Input DataFrame.

    mandatory_columns : list
        List of mandatory columns.

    Returns:
    -------
    valid_df : DataFrame
        Records without NULL values.

    invalid_df : DataFrame
        Records containing NULL values in mandatory columns.
    """

    # Build NULL validation condition
    null_condition = reduce(
        lambda x, y: x | y,
        [col(column).isNull() for column in mandatory_columns]
    )

    # Split DataFrame
    invalid_df = df.filter(null_condition)

    valid_df = df.filter(~null_condition)

    return valid_df, invalid_df