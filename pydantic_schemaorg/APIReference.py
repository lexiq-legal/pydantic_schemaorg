from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.TechArticle import TechArticle


class APIReference(TechArticle):
    """Reference documentation for application programming interfaces (APIs).

    See: https://schema.org/APIReference
    Model depth: 5
    """
    type_: str = Field(default="APIReference", alias='@type')
    assemblyVersion: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Associated product/technology version. e.g., .NET Framework 4.5.",
    )
    programmingModel: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Indicates whether API is managed or unmanaged.",
    )
    assembly: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Library file name e.g., mscorlib.dll, system.web.dll.",
    )
    executableLibraryName: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Library file name e.g., mscorlib.dll, system.web.dll.",
    )
    targetPlatform: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Type of app development: phone, Metro style, desktop, XBox, etc.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
