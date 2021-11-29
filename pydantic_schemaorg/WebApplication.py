from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.SoftwareApplication import SoftwareApplication


class WebApplication(SoftwareApplication):
    """Web applications.

    See https://schema.org/WebApplication.

    """

    browserRequirements: Optional[Union[List[str], str]] = Field(
        None,
        description="Specifies browser requirements in human-readable text. For example, 'requires HTML5"
     "support'.",
    )
    locals().update({"@type": Field("WebApplication", const=True)})


WebApplication.update_forward_refs()
