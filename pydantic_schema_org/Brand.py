from pydantic import AnyUrl, Field
from typing import Any, Optional, Union, List
from pydantic_schema_org.ImageObject import ImageObject
from pydantic_schema_org.Review import Review
from pydantic_schema_org.Intangible import Intangible


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
