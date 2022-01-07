from pydantic import AnyUrl, Field, StrictBool
from pydantic_schemaorg.Menu import Menu
from typing import List, Optional, Any, Union
from pydantic_schemaorg.Rating import Rating
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class FoodEstablishment(LocalBusiness):
    """A food-related business.

    See https://schema.org/FoodEstablishment.

    """
    type_: str = Field("FoodEstablishment", const=True, alias='@type')
    menu: Optional[Union[List[Union[AnyUrl, str, Menu]], Union[AnyUrl, str, Menu]]] = Field(
        None,
        description="Either the actual menu as a structured representation, as text, or a URL of the menu.",
    )
    starRating: Optional[Union[List[Union[Rating, str]], Union[Rating, str]]] = Field(
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
    hasMenu: Optional[Union[List[Union[AnyUrl, str, Menu]], Union[AnyUrl, str, Menu]]] = Field(
        None,
        description="Either the actual menu as a structured representation, as text, or a URL of the menu.",
    )
    servesCuisine: Optional[Union[List[str], str]] = Field(
        None,
        description="The cuisine of the restaurant.",
    )
    

FoodEstablishment.update_forward_refs()
