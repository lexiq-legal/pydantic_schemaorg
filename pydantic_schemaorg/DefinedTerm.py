from pydantic import AnyUrl, Field
from typing import List, Optional, Union
from pydantic_schemaorg.DefinedTermSet import DefinedTermSet
from pydantic_schemaorg.Intangible import Intangible


class DefinedTerm(Intangible):
    """A word, name, acronym, phrase, etc. with a formal definition. Often used in the context"
     "of category or subject classification, glossaries or dictionaries, product or creative"
     "work types, etc. Use the name property for the term being defined, use termCode if the"
     "term has an alpha-numeric code allocated, use description to provide the definition"
     "of the term.

    See https://schema.org/DefinedTerm.

    """
    type_: str = Field("DefinedTerm", const=True, alias='@type')
    termCode: Optional[Union[List[str], str]] = Field(
        None,
        description="A code that identifies this [[DefinedTerm]] within a [[DefinedTermSet]]",
    )
    inDefinedTermSet: Optional[Union[List[Union[AnyUrl, DefinedTermSet, str]], Union[AnyUrl, DefinedTermSet, str]]] = Field(
        None,
        description="A [[DefinedTermSet]] that contains this term.",
    )
    

DefinedTerm.update_forward_refs()
