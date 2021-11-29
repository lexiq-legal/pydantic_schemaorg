from pydantic import Field, AnyUrl, StrictBool
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory
from typing import Any, Union, List, Optional
from datetime import date, datetime, time
from pydantic_schemaorg.Place import Place
from pydantic_schemaorg.Intangible import Intangible


class ActionAccessSpecification(Intangible):
    """A set of requirements that a must be fulfilled in order to perform an Action.

    See https://schema.org/ActionAccessSpecification.

    """

    category: Optional[Union[List[Union[AnyUrl, str, Thing, PhysicalActivityCategory]], Union[AnyUrl, str, Thing, PhysicalActivityCategory]]] = Field(
        None,
        description="A category for the item. Greater signs or slashes can be used to informally indicate a"
     "category hierarchy.",
    )
    availabilityStarts: Optional[Union[List[Union[datetime, time, date]], Union[datetime, time, date]]] = Field(
        None,
        description="The beginning of the availability of the product or service included in the offer.",
    )
    eligibleRegion: Union[List[Union[str, Place, Any]], Union[str, Place, Any]] = Field(
        None,
        description="The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for"
     "the geo-political region(s) for which the offer or delivery charge specification is"
     "valid. See also [[ineligibleRegion]].",
    )
    requiresSubscription: Union[List[Union[StrictBool, Any]], Union[StrictBool, Any]] = Field(
        None,
        description="Indicates if use of the media require a subscription (either paid or free). Allowed values"
     "are ```true``` or ```false``` (note that an earlier version had 'yes', 'no').",
    )
    expectsAcceptanceOf: Any = Field(
        None,
        description="An Offer which must be accepted before the user can perform the Action. For example, the"
     "user may need to buy a movie before being able to watch it.",
    )
    availabilityEnds: Optional[Union[List[Union[datetime, time, date]], Union[datetime, time, date]]] = Field(
        None,
        description="The end of the availability of the product or service included in the offer.",
    )
    ineligibleRegion: Union[List[Union[str, Place, Any]], Union[str, Place, Any]] = Field(
        None,
        description="The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for"
     "the geo-political region(s) for which the offer or delivery charge specification is"
     "not valid, e.g. a region where the transaction is not allowed. See also [[eligibleRegion]].",
    )
    locals().update({"@type": Field("ActionAccessSpecification", const=True)})


ActionAccessSpecification.update_forward_refs()
