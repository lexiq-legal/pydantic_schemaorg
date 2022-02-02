from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.DataType import DataType


class Time(DataType):
    """A point in time recurring on multiple days in the form hh:mm:ss[Z|(+|-)hh:mm] (see [XML"
     "schema for details](http://www.w3.org/TR/xmlschema-2/#time)).

    See: https://schema.org/Time
    Model depth: 5
    """
    type_: str = Field("Time", alias='@type')
    

