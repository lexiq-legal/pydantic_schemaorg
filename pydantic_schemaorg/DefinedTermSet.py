from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class DefinedTermSet(CreativeWork):
    """A set of defined terms for example a set of categories or a classification scheme, a glossary,"
     "dictionary or enumeration.

    See: https://schema.org/DefinedTermSet
    Model depth: 3
    """
    type_: str = Field(default="DefinedTermSet", alias='@type')
    hasDefinedTerm: Optional[Union[List[Union['DefinedTerm', str]], 'DefinedTerm', str]] = Field(
        default=None,
        description="A Defined Term contained in this term set.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.DefinedTerm import DefinedTerm
