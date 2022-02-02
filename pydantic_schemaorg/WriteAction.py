from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.CreateAction import CreateAction


class WriteAction(CreateAction):
    """The act of authoring written creative content.

    See: https://schema.org/WriteAction
    Model depth: 4
    """
    type_: str = Field("WriteAction", alias='@type')
    language: Optional[Union[List[Union['Language', str]], 'Language', str]] = Field(
        None,
        description="A sub property of instrument. The language used on this action.",
    )
    inLanguage: Optional[Union[List[Union[str, 'Text', 'Language']], str, 'Text', 'Language']] = Field(
        None,
        description="The language of the content or performance or used in an action. Please use one of the language"
     "codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also"
     "[[availableLanguage]].",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Language import Language
    from pydantic_schemaorg.Text import Text
