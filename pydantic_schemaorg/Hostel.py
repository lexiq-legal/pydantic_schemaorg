from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.LodgingBusiness import LodgingBusiness


class Hostel(LodgingBusiness):
    """A hostel - cheap accommodation, often in shared dormitories. <br /><br /> See also the"
     "<a href=\"/docs/hotels.html\">dedicated document on the use of schema.org for marking"
     "up hotels and other forms of accommodations</a>.

    See: https://schema.org/Hostel
    Model depth: 5
    """
    type_: str = Field("Hostel", alias='@type')
    

