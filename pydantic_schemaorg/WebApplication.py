from pydantic import Field
from typing import Any, Optional, Union, List
from pydantic_schemaorg.SoftwareApplication import SoftwareApplication


class WebApplication(SoftwareApplication):
    """Web applications.

    See https://schema.org/WebApplication.

    """
    type_: str = Field("WebApplication", const=True, alias='@type')
    browserRequirements: Optional[Union[List[str], str]] = Field(
        None,
        description="Specifies browser requirements in human-readable text. For example, 'requires HTML5"
     "support'.",
    )
    

WebApplication.update_forward_refs()
