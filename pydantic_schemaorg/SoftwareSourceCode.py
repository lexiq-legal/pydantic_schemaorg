from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.CreativeWork import CreativeWork


class SoftwareSourceCode(CreativeWork):
    """Computer programming source code. Example: Full (compile ready) solutions, code snippet"
     "samples, scripts, templates.

    See: https://schema.org/SoftwareSourceCode
    Model depth: 3
    """

    type_: str = Field("SoftwareSourceCode", const=True, alias="@type")
    codeRepository: "Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]]" = Field(
        None,
        description="Link to the repository where the un-compiled, human readable code and related code is"
        "located (SVN, github, CodePlex).",
    )
    runtimePlatform: "Optional[Union[List[str], str]]" = Field(
        None,
        description="Runtime platform or script interpreter dependencies (Example - Java v1, Python2.3,"
        ".Net Framework 3.0).",
    )
    programmingLanguage: "Optional[Union[List[Union[str, ComputerLanguage]], Union[str, ComputerLanguage]]]" = Field(
        None,
        description="The computer programming language.",
    )
    runtime: "Optional[Union[List[str], str]]" = Field(
        None,
        description="Runtime platform or script interpreter dependencies (Example - Java v1, Python2.3,"
        ".Net Framework 3.0).",
    )
    codeSampleType: "Optional[Union[List[str], str]]" = Field(
        None,
        description="What type of code sample: full (compile ready) solution, code snippet, inline code,"
        "scripts, template.",
    )
    sampleType: "Optional[Union[List[str], str]]" = Field(
        None,
        description="What type of code sample: full (compile ready) solution, code snippet, inline code,"
        "scripts, template.",
    )
    targetProduct: "Optional[Union[List[Union[SoftwareApplication, str]], Union[SoftwareApplication, str]]]" = Field(
        None,
        description="Target Operating System / Product to which the code applies. If applies to several versions,"
        "just the product name can be used.",
    )


if TYPE_CHECKING:

    from pydantic import AnyUrl

    from pydantic_schemaorg.ComputerLanguage import ComputerLanguage

    from pydantic_schemaorg.SoftwareApplication import SoftwareApplication

    SoftwareSourceCode.update_forward_refs()
