from pydantic import Field, AnyUrl
from pydantic_schemaorg.CreativeWork import CreativeWork
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Service import Service


class WebAPI(Service):
    """An application programming interface accessible over Web/Internet technologies.

    See https://schema.org/WebAPI.

    """

    documentation: Optional[Union[List[Union[AnyUrl, CreativeWork]], Union[AnyUrl, CreativeWork]]] = Field(
        None,
        description="Further documentation describing the Web API in more detail.",
    )
    locals().update({"@type": Field("WebAPI", const=True)})


WebAPI.update_forward_refs()
