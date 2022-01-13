from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.LodgingBusiness import LodgingBusiness


class BedAndBreakfast(LodgingBusiness):
    """Bed and breakfast. <br /><br /> See also the <a href=\"/docs/hotels.html\">dedicated"
     "document on the use of schema.org for marking up hotels and other forms of accommodations</a>.

    See: https://schema.org/BedAndBreakfast
    Model depth: 5
    """

    type_: str = Field("BedAndBreakfast", const=True, alias="@type")


if TYPE_CHECKING:

    BedAndBreakfast.update_forward_refs()
