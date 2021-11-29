from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Audience import Audience


class EducationalAudience(Audience):
    """An EducationalAudience.

    See https://schema.org/EducationalAudience.

    """

    educationalRole: Optional[Union[List[str], str]] = Field(
        None,
        description="An educationalRole of an EducationalAudience.",
    )
    locals().update({"@type": Field("EducationalAudience", const=True)})


EducationalAudience.update_forward_refs()
