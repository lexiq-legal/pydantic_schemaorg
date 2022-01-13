from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.Accommodation import Accommodation


class House(Accommodation):
    """A house is a building or structure that has the ability to be occupied for habitation by"
     "humans or other creatures (Source: Wikipedia, the free encyclopedia, see <a href=\"http://en.wikipedia.org/wiki/House\">http://en.wikipedia.org/wiki/House</a>).

    See: https://schema.org/House
    Model depth: 4
    """

    type_: str = Field("House", const=True, alias="@type")
    numberOfRooms: "Optional[Union[List[Union[Decimal, QuantitativeValue, str]], Union[Decimal, QuantitativeValue, str]]]" = Field(
        None,
        description="The number of rooms (excluding bathrooms and closets) of the accommodation or lodging"
        "business. Typical unit code(s): ROM for room or C62 for no unit. The type of room can be"
        "put in the unitText property of the QuantitativeValue.",
    )


if TYPE_CHECKING:

    from decimal import Decimal

    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue

    House.update_forward_refs()
