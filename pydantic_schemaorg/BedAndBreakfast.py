from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.LodgingBusiness import LodgingBusiness


class BedAndBreakfast(LodgingBusiness):
    """Bed and breakfast. <br /><br /> See also the <a href=\"/docs/hotels.html\">dedicated"
     "document on the use of schema.org for marking up hotels and other forms of accommodations</a>.

    See: https://schema.org/BedAndBreakfast
    Model depth: 5
    """
    type_: str = Field("BedAndBreakfast", alias='@type')
    

