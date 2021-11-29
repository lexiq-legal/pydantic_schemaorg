from pydantic import Field
from datetime import date, datetime
from typing import Any, Union, List, Optional
from pydantic_schemaorg.PropertyValue import PropertyValue


class LocationFeatureSpecification(PropertyValue):
    """Specifies a location feature by providing a structured value representing a feature"
     "of an accommodation as a property-value pair of varying degrees of formality.

    See https://schema.org/LocationFeatureSpecification.

    """

    validFrom: Optional[Union[List[Union[datetime, date]], Union[datetime, date]]] = Field(
        None,
        description="The date when the item becomes valid.",
    )
    validThrough: Optional[Union[List[Union[datetime, date]], Union[datetime, date]]] = Field(
        None,
        description="The date after when the item is not valid. For example the end of an offer, salary period,"
     "or a period of opening hours.",
    )
    hoursAvailable: Any = Field(
        None,
        description="The hours during which this service or contact is available.",
    )
    locals().update({"@type": Field("LocationFeatureSpecification", const=True)})


LocationFeatureSpecification.update_forward_refs()
