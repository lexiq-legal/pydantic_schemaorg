from pydantic import Field
from pydantic_schemaorg.Class import Class


class DataType(Class):
    """The basic data types such as Integers, Strings, etc.

    See https://schema.org/DataType.

    """
    type_: str = Field("DataType", const=True, alias='@type')
    

DataType.update_forward_refs()
