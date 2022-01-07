from pydantic import AnyUrl, Field
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory
from typing import List, Optional, Union
from pydantic_schemaorg.Review import Review


class Recommendation(Review):
    """[[Recommendation]] is a type of [[Review]] that suggests or proposes something as the"
     "best option or best course of action. Recommendations may be for products or services,"
     "or other concrete things, as in the case of a ranked list or product guide. A [[Guide]]"
     "may list multiple recommendations for different categories. For example, in a [[Guide]]"
     "about which TVs to buy, the author may have several [[Recommendation]]s.

    See https://schema.org/Recommendation.

    """
    type_: str = Field("Recommendation", const=True, alias='@type')
    category: Optional[Union[List[Union[AnyUrl, str, Thing, PhysicalActivityCategory]], Union[AnyUrl, str, Thing, PhysicalActivityCategory]]] = Field(
        None,
        description="A category for the item. Greater signs or slashes can be used to informally indicate a"
     "category hierarchy.",
    )
    

Recommendation.update_forward_refs()
