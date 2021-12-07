from pydantic import Field
from pydantic_schemaorg.DefinedTerm import DefinedTerm
from typing import Any, Optional, Union, List
from pydantic_schemaorg.CreativeWork import CreativeWork


class DefinedTermSet(CreativeWork):
    """A set of defined terms for example a set of categories or a classification scheme, a glossary,"
     "dictionary or enumeration.

    See https://schema.org/DefinedTermSet.

    """
    type_: str = Field("DefinedTermSet", const=True, alias='@type')
    hasDefinedTerm: Optional[Union[List[DefinedTerm], DefinedTerm]] = Field(
        None,
        description="A Defined Term contained in this term set.",
    )
    

DefinedTermSet.update_forward_refs()
