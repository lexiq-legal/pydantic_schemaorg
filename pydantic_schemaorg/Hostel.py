from pydantic import Field
from pydantic_schemaorg.LodgingBusiness import LodgingBusiness


class Hostel(LodgingBusiness):
    """A hostel - cheap accommodation, often in shared dormitories. <br /><br /> See also the"
     "<a href=\"/docs/hotels.html\">dedicated document on the use of schema.org for marking"
     "up hotels and other forms of accommodations</a>.

    See https://schema.org/Hostel.

    """

    locals().update({"@type": Field("Hostel", const=True)})


Hostel.update_forward_refs()
