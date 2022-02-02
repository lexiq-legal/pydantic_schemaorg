from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.Trip import Trip


class TouristTrip(Trip):
    """A tourist trip. A created itinerary of visits to one or more places of interest ([[TouristAttraction]]/[[TouristDestination]])"
     "often linked by a similar theme, geographic area, or interest to a particular [[touristType]]."
     "The [UNWTO](http://www2.unwto.org/) defines tourism trip as the Trip taken by visitors."
     "(See examples below).

    See: https://schema.org/TouristTrip
    Model depth: 4
    """
    type_: str = Field("TouristTrip", alias='@type')
    touristType: Optional[Union[List[Union[str, 'Text', 'Audience']], str, 'Text', 'Audience']] = Field(
        None,
        description="Attraction suitable for type(s) of tourist. eg. Children, visitors from a particular"
     "country, etc.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Audience import Audience
