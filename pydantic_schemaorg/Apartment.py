from __future__ import annotations
from typing import TYPE_CHECKING

from decimal import Decimal
from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.Accommodation import Accommodation


class Apartment(Accommodation):
    """An apartment (in American English) or flat (in British English) is a self-contained"
     "housing unit (a type of residential real estate) that occupies only part of a building"
     "(Source: Wikipedia, the free encyclopedia, see <a href=\"http://en.wikipedia.org/wiki/Apartment\">http://en.wikipedia.org/wiki/Apartment</a>).

    See: https://schema.org/Apartment
    Model depth: 4
    """
    type_: str = Field("Apartment", alias='@type')
    numberOfRooms: Optional[Union[List[Union[Decimal, 'Number', 'QuantitativeValue', str]], Decimal, 'Number', 'QuantitativeValue', str]] = Field(
        None,
        description="The number of rooms (excluding bathrooms and closets) of the accommodation or lodging"
     "business. Typical unit code(s): ROM for room or C62 for no unit. The type of room can be"
     "put in the unitText property of the QuantitativeValue.",
    )
    occupancy: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        None,
        description="The allowed total occupancy for the accommodation in persons (including infants etc)."
     "For individual accommodations, this is not necessarily the legal maximum but defines"
     "the permitted usage as per the contractual agreement (e.g. a double room used by a single"
     "person). Typical unit code(s): C62 for person",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
