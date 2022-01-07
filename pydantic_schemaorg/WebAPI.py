from pydantic import AnyUrl, Field
from pydantic_schemaorg.CreativeWork import CreativeWork
from typing import List, Optional, Union
from pydantic_schemaorg.Service import Service


class WebAPI(Service):
    """An application programming interface accessible over Web/Internet technologies.

    See https://schema.org/WebAPI.

    """
    type_: str = Field("WebAPI", const=True, alias='@type')
    documentation: Optional[Union[List[Union[AnyUrl, CreativeWork, str]], Union[AnyUrl, CreativeWork, str]]] = Field(
        None,
        description="Further documentation describing the Web API in more detail.",
    )
    

WebAPI.update_forward_refs()
