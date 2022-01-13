from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.DataType import DataType


class DateTime(DataType):
    """A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]"
     "(see Chapter 5.4 of ISO 8601).

    See: https://schema.org/DateTime
    Model depth: 5
    """

    type_: str = Field("DateTime", const=True, alias="@type")


if TYPE_CHECKING:

    DateTime.update_forward_refs()
