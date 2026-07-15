from pyspark.sql import DataFrame
from pyspark.sql.types import (
    IntegerType,
    StringType,
    DoubleType,
    DateType
)


def schema_validation(df: DataFrame):
    """
    Validates DataFrame schema against expected schema.

    Parameters
    ----------
    df : DataFrame
        Input DataFrame

    Returns
    -------
    bool
        True if schema matches

    Raises
    ------
    TypeError
        If any column has incorrect datatype.
    """

    expected_schema = {
        "scheme_code": IntegerType(),
        "scheme_name": StringType(),
        "fund_house": StringType(),
        "category": StringType(),
        "nav": DoubleType(),
        "nav_date": DateType()
    }

    actual_schema = {
        field.name: field.dataType
        for field in df.schema.fields
    }

    for column, expected_type in expected_schema.items():

        if column not in actual_schema:
            raise TypeError(f"Missing column: {column}")

        actual_type = actual_schema[column]

        if type(actual_type) != type(expected_type):
            raise TypeError(
                f"Column '{column}' has datatype "
                f"{actual_type}. Expected {expected_type}."
            )

    print("✅ Schema validation passed.")

    return True