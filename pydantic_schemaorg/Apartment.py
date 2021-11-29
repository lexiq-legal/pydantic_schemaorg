from pydantic import Field
from decimal import Decimal
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Accommodation import Accommodation


class Apartment(Accommodation):
    """An apartment (in American English) or flat (in British English) is a self-contained"
     "housing unit (a type of residential real estate) that occupies only part of a building"
     "(Source: Wikipedia, the free encyclopedia, see <a href=\"http://en.wikipedia.org/wiki/Apartment\">http://en.wikipedia.org/wiki/Apartment</a>).

    See https://schema.org/Apartment.

    """

    numberOfRooms: Union[List[Union[Decimal, Any]], Union[Decimal, Any]] = Field(
        None,
        description="The number of rooms (excluding bathrooms and closets) of the accommodation or lodging"
     "business. Typical unit code(s): ROM for room or C62 for no unit. The type of room can be"
     "put in the unitText property of the QuantitativeValue.",
    )
    occupancy: Any = Field(
        None,
        description="The allowed total occupancy for the accommodation in persons (including infants etc)."
     "For individual accommodations, this is not necessarily the legal maximum but defines"
     "the permitted usage as per the contractual agreement (e.g. a double room used by a single"
     "person). Typical unit code(s): C62 for person",
    )
    locals().update({"@type": Field("Apartment", const=True)})


Apartment.update_forward_refs()
