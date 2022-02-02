from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic import AnyUrl
from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.Service import Service


class WebAPI(Service):
    """An application programming interface accessible over Web/Internet technologies.

    See: https://schema.org/WebAPI
    Model depth: 4
    """
    type_: str = Field("WebAPI", alias='@type')
    documentation: Optional[Union[List[Union[AnyUrl, 'URL', 'CreativeWork', str]], AnyUrl, 'URL', 'CreativeWork', str]] = Field(
        None,
        description="Further documentation describing the Web API in more detail.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.CreativeWork import CreativeWork
