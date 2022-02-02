from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic import AnyUrl
from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class SoftwareSourceCode(CreativeWork):
    """Computer programming source code. Example: Full (compile ready) solutions, code snippet"
     "samples, scripts, templates.

    See: https://schema.org/SoftwareSourceCode
    Model depth: 3
    """
    type_: str = Field("SoftwareSourceCode", alias='@type')
    codeRepository: Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]] = Field(
        None,
        description="Link to the repository where the un-compiled, human readable code and related code is"
     "located (SVN, github, CodePlex).",
    )
    runtimePlatform: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Runtime platform or script interpreter dependencies (Example - Java v1, Python2.3,"
     ".Net Framework 3.0).",
    )
    programmingLanguage: Optional[Union[List[Union[str, 'Text', 'ComputerLanguage']], str, 'Text', 'ComputerLanguage']] = Field(
        None,
        description="The computer programming language.",
    )
    runtime: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Runtime platform or script interpreter dependencies (Example - Java v1, Python2.3,"
     ".Net Framework 3.0).",
    )
    codeSampleType: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="What type of code sample: full (compile ready) solution, code snippet, inline code,"
     "scripts, template.",
    )
    sampleType: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="What type of code sample: full (compile ready) solution, code snippet, inline code,"
     "scripts, template.",
    )
    targetProduct: Optional[Union[List[Union['SoftwareApplication', str]], 'SoftwareApplication', str]] = Field(
        None,
        description="Target Operating System / Product to which the code applies. If applies to several versions,"
     "just the product name can be used.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.ComputerLanguage import ComputerLanguage
    from pydantic_schemaorg.SoftwareApplication import SoftwareApplication
