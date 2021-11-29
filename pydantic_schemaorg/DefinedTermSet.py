from pydantic import Field
from pydantic_schemaorg.DefinedTerm import DefinedTerm
from typing import Any, Union, List, Optional
from pydantic_schemaorg.CreativeWork import CreativeWork


class DefinedTermSet(CreativeWork):
    """A set of defined terms for example a set of categories or a classification scheme, a glossary,"
     "dictionary or enumeration.

    See https://schema.org/DefinedTermSet.

    """

    hasDefinedTerm: Optional[Union[List[DefinedTerm], DefinedTerm]] = Field(
        None,
        description="A Defined Term contained in this term set.",
    )
    locals().update({"@type": Field("DefinedTermSet", const=True)})


DefinedTermSet.update_forward_refs()
