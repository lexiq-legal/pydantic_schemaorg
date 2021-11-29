from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.CreativeWork import CreativeWork


class Guide(CreativeWork):
    """[[Guide]] is a page or article that recommend specific products or services, or aspects"
     "of a thing for a user to consider. A [[Guide]] may represent a Buying Guide and detail aspects"
     "of products or services for a user to consider. A [[Guide]] may represent a Product Guide"
     "and recommend specific products or services. A [[Guide]] may represent a Ranked List"
     "and recommend specific products or services with ranking.

    See https://schema.org/Guide.

    """

    reviewAspect: Optional[Union[List[str], str]] = Field(
        None,
        description="This Review or Rating is relevant to this part or facet of the itemReviewed.",
    )
    locals().update({"@type": Field("Guide", const=True)})


Guide.update_forward_refs()
