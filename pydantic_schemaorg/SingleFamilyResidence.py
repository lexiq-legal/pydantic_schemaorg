from __future__ import annotations
from typing import TYPE_CHECKING

from decimal import Decimal
from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.House import House


class SingleFamilyResidence(House):
    """Residence type: Single-family home.

    See: https://schema.org/SingleFamilyResidence
    Model depth: 5
    """
    type_: str = Field("SingleFamilyResidence", alias='@type')
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
