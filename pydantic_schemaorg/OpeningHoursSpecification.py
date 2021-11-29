from pydantic import Field
from datetime import date, datetime, time
from typing import Any, Union, List, Optional
from pydantic_schemaorg.DayOfWeek import DayOfWeek
from pydantic_schemaorg.StructuredValue import StructuredValue


class OpeningHoursSpecification(StructuredValue):
    """A structured value providing information about the opening hours of a place or a certain"
     "service inside a place. The place is __open__ if the [[opens]] property is specified,"
     "and __closed__ otherwise. If the value for the [[closes]] property is less than the value"
     "for the [[opens]] property then the hour range is assumed to span over the next day.

    See https://schema.org/OpeningHoursSpecification.

    """

    opens: Optional[Union[List[time], time]] = Field(
        None,
        description="The opening hour of the place or service on the given day(s) of the week.",
    )
    validFrom: Optional[Union[List[Union[datetime, date]], Union[datetime, date]]] = Field(
        None,
        description="The date when the item becomes valid.",
    )
    validThrough: Optional[Union[List[Union[datetime, date]], Union[datetime, date]]] = Field(
        None,
        description="The date after when the item is not valid. For example the end of an offer, salary period,"
     "or a period of opening hours.",
    )
    closes: Optional[Union[List[time], time]] = Field(
        None,
        description="The closing hour of the place or service on the given day(s) of the week.",
    )
    dayOfWeek: Optional[Union[List[DayOfWeek], DayOfWeek]] = Field(
        None,
        description="The day of the week for which these opening hours are valid.",
    )
    locals().update({"@type": Field("OpeningHoursSpecification", const=True)})


OpeningHoursSpecification.update_forward_refs()
