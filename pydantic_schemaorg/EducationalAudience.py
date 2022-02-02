from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.Audience import Audience


class EducationalAudience(Audience):
    """An EducationalAudience.

    See: https://schema.org/EducationalAudience
    Model depth: 4
    """
    type_: str = Field("EducationalAudience", alias='@type')
    educationalRole: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="An educationalRole of an EducationalAudience.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
