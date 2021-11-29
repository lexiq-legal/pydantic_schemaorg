from pydantic import Field
from pydantic_schemaorg.Audience import Audience
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Trip import Trip


class TouristTrip(Trip):
    """A tourist trip. A created itinerary of visits to one or more places of interest ([[TouristAttraction]]/[[TouristDestination]])"
     "often linked by a similar theme, geographic area, or interest to a particular [[touristType]]."
     "The [UNWTO](http://www2.unwto.org/) defines tourism trip as the Trip taken by visitors."
     "(See examples below).

    See https://schema.org/TouristTrip.

    """

    touristType: Optional[Union[List[Union[str, Audience]], Union[str, Audience]]] = Field(
        None,
        description="Attraction suitable for type(s) of tourist. eg. Children, visitors from a particular"
     "country, etc.",
    )
    locals().update({"@type": Field("TouristTrip", const=True)})


TouristTrip.update_forward_refs()
