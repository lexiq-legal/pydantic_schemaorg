from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

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

    type_: str = Field("Recommendation", const=True, alias="@type")
    category: "Optional[Union[List[Union[AnyUrl, str, PhysicalActivityCategory, Thing]], Union[AnyUrl, str, PhysicalActivityCategory, Thing]]]" = Field(
        None,
        description="A category for the item. Greater signs or slashes can be used to informally indicate a"
        "category hierarchy.",
    )


if TYPE_CHECKING:

    from pydantic import AnyUrl

    from pydantic_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory

    from pydantic_schemaorg.Thing import Thing

    Recommendation.update_forward_refs()
