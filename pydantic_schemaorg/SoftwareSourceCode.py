from pydantic import Field, AnyUrl
from typing import Any, Union, List, Optional
from pydantic_schemaorg.SoftwareApplication import SoftwareApplication
from pydantic_schemaorg.CreativeWork import CreativeWork


class SoftwareSourceCode(CreativeWork):
    """Computer programming source code. Example: Full (compile ready) solutions, code snippet"
     "samples, scripts, templates.

    See https://schema.org/SoftwareSourceCode.

    """

    codeRepository: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None,
        description="Link to the repository where the un-compiled, human readable code and related code is"
     "located (SVN, github, CodePlex).",
    )
    runtimePlatform: Optional[Union[List[str], str]] = Field(
        None,
        description="Runtime platform or script interpreter dependencies (Example - Java v1, Python2.3,"
     ".Net Framework 3.0).",
    )
    programmingLanguage: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="The computer programming language.",
    )
    runtime: Optional[Union[List[str], str]] = Field(
        None,
        description="Runtime platform or script interpreter dependencies (Example - Java v1, Python2.3,"
     ".Net Framework 3.0).",
    )
    codeSampleType: Optional[Union[List[str], str]] = Field(
        None,
        description="What type of code sample: full (compile ready) solution, code snippet, inline code,"
     "scripts, template.",
    )
    sampleType: Optional[Union[List[str], str]] = Field(
        None,
        description="What type of code sample: full (compile ready) solution, code snippet, inline code,"
     "scripts, template.",
    )
    targetProduct: Optional[Union[List[SoftwareApplication], SoftwareApplication]] = Field(
        None,
        description="Target Operating System / Product to which the code applies. If applies to several versions,"
     "just the product name can be used.",
    )
    locals().update({"@type": Field("SoftwareSourceCode", const=True)})


SoftwareSourceCode.update_forward_refs()
