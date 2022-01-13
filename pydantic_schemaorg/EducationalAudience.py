from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.Audience import Audience


class EducationalAudience(Audience):
    """An EducationalAudience.

    See: https://schema.org/EducationalAudience
    Model depth: 4
    """

    type_: str = Field("EducationalAudience", const=True, alias="@type")
    educationalRole: "Optional[Union[List[str], str]]" = Field(
        None,
        description="An educationalRole of an EducationalAudience.",
    )


if TYPE_CHECKING:

    EducationalAudience.update_forward_refs()
