from pydantic import Field
from pydantic_schemaorg.TouristAttraction import TouristAttraction
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Audience import Audience
from pydantic_schemaorg.Place import Place


class TouristDestination(Place):
    """A tourist destination. In principle any [[Place]] can be a [[TouristDestination]]"
     "from a [[City]], Region or [[Country]] to an [[AmusementPark]] or [[Hotel]]. This Type"
     "can be used on its own to describe a general [[TouristDestination]], or be used as an [[additionalType]]"
     "to add tourist relevant properties to any other [[Place]]. A [[TouristDestination]]"
     "is defined as a [[Place]] that contains, or is colocated with, one or more [[TouristAttraction]]s,"
     "often linked by a similar theme or interest to a particular [[touristType]]. The [UNWTO](http://www2.unwto.org/)"
     "defines Destination (main destination of a tourism trip) as the place visited that is"
     "central to the decision to take the trip. (See examples below).

    See https://schema.org/TouristDestination.

    """

    includesAttraction: Optional[Union[List[TouristAttraction], TouristAttraction]] = Field(
        None,
        description="Attraction located at destination.",
    )
    touristType: Optional[Union[List[Union[str, Audience]], Union[str, Audience]]] = Field(
        None,
        description="Attraction suitable for type(s) of tourist. eg. Children, visitors from a particular"
     "country, etc.",
    )
    locals().update({"@type": Field("TouristDestination", const=True)})


TouristDestination.update_forward_refs()
