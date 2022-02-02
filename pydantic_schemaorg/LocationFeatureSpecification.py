from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.PropertyValue import PropertyValue


class LocationFeatureSpecification(PropertyValue):
    """Specifies a location feature by providing a structured value representing a feature"
     "of an accommodation as a property-value pair of varying degrees of formality.

    See: https://schema.org/LocationFeatureSpecification
    Model depth: 5
    """
    type_: str = Field("LocationFeatureSpecification", alias='@type')
    validFrom: Optional[Union[List[Union[ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]], ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]] = Field(
        None,
        description="The date when the item becomes valid.",
    )
    validThrough: Optional[Union[List[Union[ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]], ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]] = Field(
        None,
        description="The date after when the item is not valid. For example the end of an offer, salary period,"
     "or a period of opening hours.",
    )
    hoursAvailable: Optional[Union[List[Union['OpeningHoursSpecification', str]], 'OpeningHoursSpecification', str]] = Field(
        None,
        description="The hours during which this service or contact is available.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.OpeningHoursSpecification import OpeningHoursSpecification
