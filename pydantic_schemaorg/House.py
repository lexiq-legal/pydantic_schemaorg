from pydantic import Field
from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
from decimal import Decimal
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Accommodation import Accommodation


class House(Accommodation):
    """A house is a building or structure that has the ability to be occupied for habitation by"
     "humans or other creatures (Source: Wikipedia, the free encyclopedia, see <a href=\"http://en.wikipedia.org/wiki/House\">http://en.wikipedia.org/wiki/House</a>).

    See https://schema.org/House.

    """

    numberOfRooms: Optional[Union[List[Union[Decimal, QuantitativeValue]], Union[Decimal, QuantitativeValue]]] = Field(
        None,
        description="The number of rooms (excluding bathrooms and closets) of the accommodation or lodging"
     "business. Typical unit code(s): ROM for room or C62 for no unit. The type of room can be"
     "put in the unitText property of the QuantitativeValue.",
    )
    locals().update({"@type": Field("House", const=True)})


House.update_forward_refs()
