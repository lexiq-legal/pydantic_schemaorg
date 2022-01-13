from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.Intangible import Intangible


class Brand(Intangible):
    """A brand is a name used by an organization or business person for labeling a product, product"
     "group, or similar.

    See: https://schema.org/Brand
    Model depth: 3
    """

    type_: str = Field("Brand", const=True, alias="@type")
    aggregateRating: "Optional[Union[List[Union[AggregateRating, str]], Union[AggregateRating, str]]]" = Field(
        None,
        description="The overall rating, based on a collection of reviews or ratings, of the item.",
    )
    slogan: "Optional[Union[List[str], str]]" = Field(
        None,
        description="A slogan or motto associated with the item.",
    )
    logo: "Optional[Union[List[Union[AnyUrl, ImageObject, str]], Union[AnyUrl, ImageObject, str]]]" = Field(
        None,
        description="An associated logo.",
    )
    review: "Optional[Union[List[Union[Review, str]], Union[Review, str]]]" = Field(
        None,
        description="A review of the item.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.AggregateRating import AggregateRating

    from pydantic import AnyUrl

    from pydantic_schemaorg.ImageObject import ImageObject

    from pydantic_schemaorg.Review import Review

    Brand.update_forward_refs()
