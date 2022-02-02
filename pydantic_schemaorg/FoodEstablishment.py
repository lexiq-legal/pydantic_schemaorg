from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic import StrictBool, AnyUrl
from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class FoodEstablishment(LocalBusiness):
    """A food-related business.

    See: https://schema.org/FoodEstablishment
    Model depth: 4
    """
    type_: str = Field("FoodEstablishment", alias='@type')
    menu: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'Menu']], AnyUrl, 'URL', str, 'Text', 'Menu']] = Field(
        None,
        description="Either the actual menu as a structured representation, as text, or a URL of the menu.",
    )
    starRating: Optional[Union[List[Union['Rating', str]], 'Rating', str]] = Field(
        None,
        description="An official rating for a lodging business or food establishment, e.g. from national"
     "associations or standards bodies. Use the author property to indicate the rating organization,"
     "e.g. as an Organization with name such as (e.g. HOTREC, DEHOGA, WHR, or Hotelstars).",
    )
    acceptsReservations: Optional[Union[List[Union[AnyUrl, 'URL', StrictBool, 'Boolean', str, 'Text']], AnyUrl, 'URL', StrictBool, 'Boolean', str, 'Text']] = Field(
        None,
        description="Indicates whether a FoodEstablishment accepts reservations. Values can be Boolean,"
     "an URL at which reservations can be made or (for backwards compatibility) the strings"
     "```Yes``` or ```No```.",
    )
    hasMenu: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'Menu']], AnyUrl, 'URL', str, 'Text', 'Menu']] = Field(
        None,
        description="Either the actual menu as a structured representation, as text, or a URL of the menu.",
    )
    servesCuisine: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The cuisine of the restaurant.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Menu import Menu
    from pydantic_schemaorg.Rating import Rating
    from pydantic_schemaorg.Boolean import Boolean
