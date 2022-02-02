from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class DefinedTerm(Intangible):
    """A word, name, acronym, phrase, etc. with a formal definition. Often used in the context"
     "of category or subject classification, glossaries or dictionaries, product or creative"
     "work types, etc. Use the name property for the term being defined, use termCode if the"
     "term has an alpha-numeric code allocated, use description to provide the definition"
     "of the term.

    See: https://schema.org/DefinedTerm
    Model depth: 3
    """
    type_: str = Field("DefinedTerm", alias='@type')
    termCode: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="A code that identifies this [[DefinedTerm]] within a [[DefinedTermSet]]",
    )
    inDefinedTermSet: Optional[Union[List[Union[AnyUrl, 'URL', 'DefinedTermSet', str]], AnyUrl, 'URL', 'DefinedTermSet', str]] = Field(
        None,
        description="A [[DefinedTermSet]] that contains this term.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.DefinedTermSet import DefinedTermSet
