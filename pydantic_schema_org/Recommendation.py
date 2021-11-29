from pydantic import AnyUrl, Field
from pydantic_schema_org.PhysicalActivityCategory import PhysicalActivityCategory
from pydantic_schema_org.Thing import Thing
from typing import Any, Optional, Union, List
from pydantic_schema_org.Review import Review


class Recommendation(Review):
    """[[Recommendation]] is a type of [[Review]] that suggests or proposes something as the"
     "best option or best course of action. Recommendations may be for products or services,"
     "or other concrete things, as in the case of a ranked list or product guide. A [[Guide]]"
     "may list multiple recommendations for different categories. For example, in a [[Guide]]"
     "about which TVs to buy, the author may have several [[Recommendation]]s.

    See https://schema.org/Recommendation.

    """

    category: Optional[Union[List[Union[AnyUrl, str, PhysicalActivityCategory, Thing]], Union[AnyUrl, str, PhysicalActivityCategory, Thing]]] = Field(
        None,
        description="A category for the item. Greater signs or slashes can be used to informally indicate a"
     "category hierarchy.",
    )
    locals().update({"@type": Field("Recommendation", const=True)})


Recommendation.update_forward_refs()
