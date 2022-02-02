from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
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

    See: https://schema.org/TouristDestination
    Model depth: 3
    """
    type_: str = Field("TouristDestination", alias='@type')
    includesAttraction: Optional[Union[List[Union['TouristAttraction', str]], 'TouristAttraction', str]] = Field(
        None,
        description="Attraction located at destination.",
    )
    touristType: Optional[Union[List[Union[str, 'Text', 'Audience']], str, 'Text', 'Audience']] = Field(
        None,
        description="Attraction suitable for type(s) of tourist. eg. Children, visitors from a particular"
     "country, etc.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.TouristAttraction import TouristAttraction
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Audience import Audience
