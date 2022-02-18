from __future__ import annotations
from typing import TYPE_CHECKING

from decimal import Decimal
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.Accommodation import Accommodation


class House(Accommodation):
    """A house is a building or structure that has the ability to be occupied for habitation by"
     "humans or other creatures (Source: Wikipedia, the free encyclopedia, see <a href=\"http://en.wikipedia.org/wiki/House\">http://en.wikipedia.org/wiki/House</a>).

    See: https://schema.org/House
    Model depth: 4
    """
    type_: str = Field(default="House", alias='@type', constant=True)
    numberOfRooms: Optional[Union[List[Union[int, float, 'Number', 'QuantitativeValue', str]], int, float, 'Number', 'QuantitativeValue', str]] = Field(
        default=None,
        description="The number of rooms (excluding bathrooms and closets) of the accommodation or lodging"
     "business. Typical unit code(s): ROM for room or C62 for no unit. The type of room can be"
     "put in the unitText property of the QuantitativeValue.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
