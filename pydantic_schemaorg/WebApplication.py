from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.SoftwareApplication import SoftwareApplication


class WebApplication(SoftwareApplication):
    """Web applications.

    See: https://schema.org/WebApplication
    Model depth: 4
    """
    type_: str = Field("WebApplication", alias='@type')
    browserRequirements: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Specifies browser requirements in human-readable text. For example, 'requires HTML5"
     "support'.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
