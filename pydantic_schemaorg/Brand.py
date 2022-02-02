from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class Brand(Intangible):
    """A brand is a name used by an organization or business person for labeling a product, product"
     "group, or similar.

    See: https://schema.org/Brand
    Model depth: 3
    """
    type_: str = Field("Brand", alias='@type')
    aggregateRating: Optional[Union[List[Union['AggregateRating', str]], 'AggregateRating', str]] = Field(
        None,
        description="The overall rating, based on a collection of reviews or ratings, of the item.",
    )
    slogan: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="A slogan or motto associated with the item.",
    )
    logo: Optional[Union[List[Union[AnyUrl, 'URL', 'ImageObject', str]], AnyUrl, 'URL', 'ImageObject', str]] = Field(
        None,
        description="An associated logo.",
    )
    review: Optional[Union[List[Union['Review', str]], 'Review', str]] = Field(
        None,
        description="A review of the item.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.AggregateRating import AggregateRating
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.Review import Review
