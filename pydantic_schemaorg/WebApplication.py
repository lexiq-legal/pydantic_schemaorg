from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.SoftwareApplication import SoftwareApplication


class WebApplication(SoftwareApplication):
    """Web applications.

    See: https://schema.org/WebApplication
    Model depth: 4
    """

    type_: str = Field("WebApplication", const=True, alias="@type")
    browserRequirements: "Optional[Union[List[str], str]]" = Field(
        None,
        description="Specifies browser requirements in human-readable text. For example, 'requires HTML5"
        "support'.",
    )


if TYPE_CHECKING:

    WebApplication.update_forward_refs()
