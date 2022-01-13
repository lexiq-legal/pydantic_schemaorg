from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.StructuredValue import StructuredValue


class OpeningHoursSpecification(StructuredValue):
    """A structured value providing information about the opening hours of a place or a certain"
     "service inside a place. The place is __open__ if the [[opens]] property is specified,"
     "and __closed__ otherwise. If the value for the [[closes]] property is less than the value"
     "for the [[opens]] property then the hour range is assumed to span over the next day.

    See: https://schema.org/OpeningHoursSpecification
    Model depth: 4
    """

    type_: str = Field("OpeningHoursSpecification", const=True, alias="@type")
    opens: "Optional[Union[List[Union[time, str]], Union[time, str]]]" = Field(
        None,
        description="The opening hour of the place or service on the given day(s) of the week.",
    )
    validFrom: "Optional[Union[List[Union[datetime, date, str]], Union[datetime, date, str]]]" = Field(
        None,
        description="The date when the item becomes valid.",
    )
    validThrough: "Optional[Union[List[Union[datetime, date, str]], Union[datetime, date, str]]]" = Field(
        None,
        description="The date after when the item is not valid. For example the end of an offer, salary period,"
        "or a period of opening hours.",
    )
    closes: "Optional[Union[List[Union[time, str]], Union[time, str]]]" = Field(
        None,
        description="The closing hour of the place or service on the given day(s) of the week.",
    )
    dayOfWeek: "Optional[Union[List[Union[DayOfWeek, str]], Union[DayOfWeek, str]]]" = (
        Field(
            None,
            description="The day of the week for which these opening hours are valid.",
        )
    )


if TYPE_CHECKING:

    from datetime import date, datetime, time

    from pydantic_schemaorg.DayOfWeek import DayOfWeek

    OpeningHoursSpecification.update_forward_refs()
