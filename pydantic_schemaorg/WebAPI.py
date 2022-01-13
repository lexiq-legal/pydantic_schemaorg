from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.Service import Service


class WebAPI(Service):
    """An application programming interface accessible over Web/Internet technologies.

    See: https://schema.org/WebAPI
    Model depth: 4
    """

    type_: str = Field("WebAPI", const=True, alias="@type")
    documentation: "Optional[Union[List[Union[AnyUrl, CreativeWork, str]], Union[AnyUrl, CreativeWork, str]]]" = Field(
        None,
        description="Further documentation describing the Web API in more detail.",
    )


if TYPE_CHECKING:

    from pydantic import AnyUrl

    from pydantic_schemaorg.CreativeWork import CreativeWork

    WebAPI.update_forward_refs()
