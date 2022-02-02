from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic import StrictBool, AnyUrl
from typing import Union, Optional, List
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from datetime import time


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class ActionAccessSpecification(Intangible):
    """A set of requirements that a must be fulfilled in order to perform an Action.

    See: https://schema.org/ActionAccessSpecification
    Model depth: 3
    """
    type_: str = Field("ActionAccessSpecification", alias='@type')
    category: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'Thing', 'PhysicalActivityCategory']], AnyUrl, 'URL', str, 'Text', 'Thing', 'PhysicalActivityCategory']] = Field(
        None,
        description="A category for the item. Greater signs or slashes can be used to informally indicate a"
     "category hierarchy.",
    )
    availabilityStarts: Optional[Union[List[Union[ISO8601Date, 'DateTime', time, 'Time', ISO8601Date, 'Date', str]], ISO8601Date, 'DateTime', time, 'Time', ISO8601Date, 'Date', str]] = Field(
        None,
        description="The beginning of the availability of the product or service included in the offer.",
    )
    eligibleRegion: Optional[Union[List[Union[str, 'Text', 'GeoShape', 'Place']], str, 'Text', 'GeoShape', 'Place']] = Field(
        None,
        description="The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for"
     "the geo-political region(s) for which the offer or delivery charge specification is"
     "valid. See also [[ineligibleRegion]].",
    )
    requiresSubscription: Optional[Union[List[Union[StrictBool, 'Boolean', 'MediaSubscription', str]], StrictBool, 'Boolean', 'MediaSubscription', str]] = Field(
        None,
        description="Indicates if use of the media require a subscription (either paid or free). Allowed values"
     "are ```true``` or ```false``` (note that an earlier version had 'yes', 'no').",
    )
    expectsAcceptanceOf: Optional[Union[List[Union['Offer', str]], 'Offer', str]] = Field(
        None,
        description="An Offer which must be accepted before the user can perform the Action. For example, the"
     "user may need to buy a movie before being able to watch it.",
    )
    availabilityEnds: Optional[Union[List[Union[ISO8601Date, 'DateTime', time, 'Time', ISO8601Date, 'Date', str]], ISO8601Date, 'DateTime', time, 'Time', ISO8601Date, 'Date', str]] = Field(
        None,
        description="The end of the availability of the product or service included in the offer.",
    )
    ineligibleRegion: Optional[Union[List[Union[str, 'Text', 'GeoShape', 'Place']], str, 'Text', 'GeoShape', 'Place']] = Field(
        None,
        description="The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for"
     "the geo-political region(s) for which the offer or delivery charge specification is"
     "not valid, e.g. a region where the transaction is not allowed. See also [[eligibleRegion]].",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Time import Time
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.GeoShape import GeoShape
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.MediaSubscription import MediaSubscription
    from pydantic_schemaorg.Offer import Offer
