from pydantic import Field
from datetime import datetime, date
from typing import List, Optional, Union
from pydantic_schemaorg.OpeningHoursSpecification import OpeningHoursSpecification
from pydantic_schemaorg.PropertyValue import PropertyValue


class LocationFeatureSpecification(PropertyValue):
    """Specifies a location feature by providing a structured value representing a feature"
     "of an accommodation as a property-value pair of varying degrees of formality.

    See https://schema.org/LocationFeatureSpecification.

    """
    type_: str = Field("LocationFeatureSpecification", const=True, alias='@type')
    validFrom: Optional[Union[List[Union[datetime, date, str]], Union[datetime, date, str]]] = Field(
        None,
        description="The date when the item becomes valid.",
    )
    validThrough: Optional[Union[List[Union[datetime, date, str]], Union[datetime, date, str]]] = Field(
        None,
        description="The date after when the item is not valid. For example the end of an offer, salary period,"
     "or a period of opening hours.",
    )
    hoursAvailable: Optional[Union[List[Union[OpeningHoursSpecification, str]], Union[OpeningHoursSpecification, str]]] = Field(
        None,
        description="The hours during which this service or contact is available.",
    )
    

LocationFeatureSpecification.update_forward_refs()
