from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.LodgingBusiness import LodgingBusiness


class Motel(LodgingBusiness):
    """A motel. <br /><br /> See also the <a href=\"/docs/hotels.html\">dedicated document"
     "on the use of schema.org for marking up hotels and other forms of accommodations</a>.

    See: https://schema.org/Motel
    Model depth: 5
    """
    type_: str = Field("Motel", alias='@type')
    

