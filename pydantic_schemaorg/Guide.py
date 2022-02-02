from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Guide(CreativeWork):
    """[[Guide]] is a page or article that recommend specific products or services, or aspects"
     "of a thing for a user to consider. A [[Guide]] may represent a Buying Guide and detail aspects"
     "of products or services for a user to consider. A [[Guide]] may represent a Product Guide"
     "and recommend specific products or services. A [[Guide]] may represent a Ranked List"
     "and recommend specific products or services with ranking.

    See: https://schema.org/Guide
    Model depth: 3
    """
    type_: str = Field("Guide", alias='@type')
    reviewAspect: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="This Review or Rating is relevant to this part or facet of the itemReviewed.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
