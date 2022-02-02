from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Class import Class


class DataType(Class):
    """The basic data types such as Integers, Strings, etc.

    See: https://schema.org/DataType
    Model depth: 4
    """
    type_: str = Field("DataType", alias='@type')
    

