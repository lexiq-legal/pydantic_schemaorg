from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.Intangible import Intangible


class EntryPoint(Intangible):
    """An entry point, within some Web-based protocol.

    See: https://schema.org/EntryPoint
    Model depth: 3
    """

    type_: str = Field("EntryPoint", const=True, alias="@type")
    contentType: "Optional[Union[List[str], str]]" = Field(
        None,
        description="The supported content type(s) for an EntryPoint response.",
    )
    actionApplication: "Optional[Union[List[Union[SoftwareApplication, str]], Union[SoftwareApplication, str]]]" = Field(
        None,
        description="An application that can complete the request.",
    )
    application: "Optional[Union[List[Union[SoftwareApplication, str]], Union[SoftwareApplication, str]]]" = Field(
        None,
        description="An application that can complete the request.",
    )
    actionPlatform: "Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]]" = Field(
        None,
        description="The high level platform(s) where the Action can be performed for the given URL. To specify"
        "a specific application or operating system instance, use actionApplication.",
    )
    encodingType: "Optional[Union[List[str], str]]" = Field(
        None,
        description="The supported encoding type(s) for an EntryPoint request.",
    )
    httpMethod: "Optional[Union[List[str], str]]" = Field(
        None,
        description="An HTTP method that specifies the appropriate HTTP method for a request to an HTTP EntryPoint."
        "Values are capitalized strings as used in HTTP.",
    )
    urlTemplate: "Optional[Union[List[str], str]]" = Field(
        None,
        description="An url template (RFC6570) that will be used to construct the target of the execution of"
        "the action.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.SoftwareApplication import SoftwareApplication

    from pydantic import AnyUrl

    EntryPoint.update_forward_refs()
