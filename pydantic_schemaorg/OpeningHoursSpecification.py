from __future__ import annotations
from typing import TYPE_CHECKING

from datetime import time
from typing import Union, Optional, List
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date


from pydantic import Field
from pydantic_schemaorg.StructuredValue import StructuredValue


class OpeningHoursSpecification(StructuredValue):
    """A structured value providing information about the opening hours of a place or a certain"
     "service inside a place. The place is __open__ if the [[opens]] property is specified,"
     "and __closed__ otherwise. If the value for the [[closes]] property is less than the value"
     "for the [[opens]] property then the hour range is assumed to span over the next day.

    See: https://schema.org/OpeningHoursSpecification
    Model depth: 4
    """
    type_: str = Field("OpeningHoursSpecification", alias='@type')
    opens: Optional[Union[List[Union[time, 'Time', str]], time, 'Time', str]] = Field(
        None,
        description="The opening hour of the place or service on the given day(s) of the week.",
    )
    validFrom: Optional[Union[List[Union[ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]], ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]] = Field(
        None,
        description="The date when the item becomes valid.",
    )
    validThrough: Optional[Union[List[Union[ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]], ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]] = Field(
        None,
        description="The date after when the item is not valid. For example the end of an offer, salary period,"
     "or a period of opening hours.",
    )
    closes: Optional[Union[List[Union[time, 'Time', str]], time, 'Time', str]] = Field(
        None,
        description="The closing hour of the place or service on the given day(s) of the week.",
    )
    dayOfWeek: Optional[Union[List[Union['DayOfWeek', str]], 'DayOfWeek', str]] = Field(
        None,
        description="The day of the week for which these opening hours are valid.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Time import Time
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.DayOfWeek import DayOfWeek
