from pydantic import Field, AnyUrl, StrictBool
from typing import Any, Union, List, Optional
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class FoodEstablishment(LocalBusiness):
    """A food-related business.

    See https://schema.org/FoodEstablishment.

    """

    menu: Union[List[Union[AnyUrl, str, Any]], Union[AnyUrl, str, Any]] = Field(
        None,
        description="Either the actual menu as a structured representation, as text, or a URL of the menu.",
    )
    starRating: Any = Field(
        None,
        description="An official rating for a lodging business or food establishment, e.g. from national"
     "associations or standards bodies. Use the author property to indicate the rating organization,"
     "e.g. as an Organization with name such as (e.g. HOTREC, DEHOGA, WHR, or Hotelstars).",
    )
    acceptsReservations: Optional[Union[List[Union[AnyUrl, str, StrictBool]], Union[AnyUrl, str, StrictBool]]] = Field(
        None,
        description="Indicates whether a FoodEstablishment accepts reservations. Values can be Boolean,"
     "an URL at which reservations can be made or (for backwards compatibility) the strings"
     "```Yes``` or ```No```.",
    )
    hasMenu: Union[List[Union[AnyUrl, str, Any]], Union[AnyUrl, str, Any]] = Field(
        None,
        description="Either the actual menu as a structured representation, as text, or a URL of the menu.",
    )
    servesCuisine: Optional[Union[List[str], str]] = Field(
        None,
        description="The cuisine of the restaurant.",
    )
    locals().update({"@type": Field("FoodEstablishment", const=True)})


FoodEstablishment.update_forward_refs()
