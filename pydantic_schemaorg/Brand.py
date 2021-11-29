from pydantic import Field, AnyUrl
from typing import Any, Union, List, Optional
from pydantic_schemaorg.ImageObject import ImageObject
from pydantic_schemaorg.Review import Review
from pydantic_schemaorg.Intangible import Intangible


class Brand(Intangible):
    """A brand is a name used by an organization or business person for labeling a product, product"
     "group, or similar.

    See https://schema.org/Brand.

    """

    aggregateRating: Any = Field(
        None,
        description="The overall rating, based on a collection of reviews or ratings, of the item.",
    )
    slogan: Optional[Union[List[str], str]] = Field(
        None,
        description="A slogan or motto associated with the item.",
    )
    logo: Optional[Union[List[Union[AnyUrl, ImageObject]], Union[AnyUrl, ImageObject]]] = Field(
        None,
        description="An associated logo.",
    )
    review: Optional[Union[List[Review], Review]] = Field(
        None,
        description="A review of the item.",
    )
    locals().update({"@type": Field("Brand", const=True)})


Brand.update_forward_refs()
