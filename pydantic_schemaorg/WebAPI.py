from pydantic import Field, AnyUrl
from pydantic_schemaorg.CreativeWork import CreativeWork
from typing import Any, Optional, Union, List
from pydantic_schemaorg.Service import Service


class WebAPI(Service):
    """An application programming interface accessible over Web/Internet technologies.

    See https://schema.org/WebAPI.

    """
    type_: str = Field("WebAPI", const=True, alias='@type')
    documentation: Optional[Union[List[Union[AnyUrl, CreativeWork]], Union[AnyUrl, CreativeWork]]] = Field(
        None,
        description="Further documentation describing the Web API in more detail.",
    )
    

WebAPI.update_forward_refs()
