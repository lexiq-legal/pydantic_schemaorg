from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.TechArticle import TechArticle


class APIReference(TechArticle):
    """Reference documentation for application programming interfaces (APIs).

    See https://schema.org/APIReference.

    """

    assemblyVersion: Optional[Union[List[str], str]] = Field(
        None,
        description="Associated product/technology version. e.g., .NET Framework 4.5.",
    )
    programmingModel: Optional[Union[List[str], str]] = Field(
        None,
        description="Indicates whether API is managed or unmanaged.",
    )
    assembly: Optional[Union[List[str], str]] = Field(
        None,
        description="Library file name e.g., mscorlib.dll, system.web.dll.",
    )
    executableLibraryName: Optional[Union[List[str], str]] = Field(
        None,
        description="Library file name e.g., mscorlib.dll, system.web.dll.",
    )
    targetPlatform: Optional[Union[List[str], str]] = Field(
        None,
        description="Type of app development: phone, Metro style, desktop, XBox, etc.",
    )
    locals().update({"@type": Field("APIReference", const=True)})


APIReference.update_forward_refs()
