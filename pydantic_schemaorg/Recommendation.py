from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic import AnyUrl
from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.Review import Review


class Recommendation(Review):
    """[[Recommendation]] is a type of [[Review]] that suggests or proposes something as the"
     "best option or best course of action. Recommendations may be for products or services,"
     "or other concrete things, as in the case of a ranked list or product guide. A [[Guide]]"
     "may list multiple recommendations for different categories. For example, in a [[Guide]]"
     "about which TVs to buy, the author may have several [[Recommendation]]s.

    See: https://schema.org/Recommendation
    Model depth: 4
    """
    type_: str = Field("Recommendation", alias='@type')
    category: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'Thing', 'PhysicalActivityCategory']], AnyUrl, 'URL', str, 'Text', 'Thing', 'PhysicalActivityCategory']] = Field(
        None,
        description="A category for the item. Greater signs or slashes can be used to informally indicate a"
     "category hierarchy.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory
