from pydantic import Field
from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
from decimal import Decimal
from typing import Any, Union, List, Optional
from pydantic_schemaorg.House import House


class SingleFamilyResidence(House):
    """Residence type: Single-family home.

    See https://schema.org/SingleFamilyResidence.

    """

    numberOfRooms: Optional[Union[List[Union[Decimal, QuantitativeValue]], Union[Decimal, QuantitativeValue]]] = Field(
        None,
        description="The number of rooms (excluding bathrooms and closets) of the accommodation or lodging"
     "business. Typical unit code(s): ROM for room or C62 for no unit. The type of room can be"
     "put in the unitText property of the QuantitativeValue.",
    )
    occupancy: Optional[Union[List[QuantitativeValue], QuantitativeValue]] = Field(
        None,
        description="The allowed total occupancy for the accommodation in persons (including infants etc)."
     "For individual accommodations, this is not necessarily the legal maximum but defines"
     "the permitted usage as per the contractual agreement (e.g. a double room used by a single"
     "person). Typical unit code(s): C62 for person",
    )
    locals().update({"@type": Field("SingleFamilyResidence", const=True)})


SingleFamilyResidence.update_forward_refs()
