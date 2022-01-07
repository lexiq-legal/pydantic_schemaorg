from pydantic import Field
from typing import List, Optional, Any, Union
from pydantic_schemaorg.Audience import Audience


class EducationalAudience(Audience):
    """An EducationalAudience.

    See https://schema.org/EducationalAudience.

    """
    type_: str = Field("EducationalAudience", const=True, alias='@type')
    educationalRole: Optional[Union[List[str], str]] = Field(
        None,
        description="An educationalRole of an EducationalAudience.",
    )
    

EducationalAudience.update_forward_refs()
