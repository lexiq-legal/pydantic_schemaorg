from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.CreativeWork import CreativeWork


class DefinedTermSet(CreativeWork):
    """A set of defined terms for example a set of categories or a classification scheme, a glossary,"
     "dictionary or enumeration.

    See: https://schema.org/DefinedTermSet
    Model depth: 3
    """

    type_: str = Field("DefinedTermSet", const=True, alias="@type")
    hasDefinedTerm: "Optional[Union[List[Union[DefinedTerm, str]], Union[DefinedTerm, str]]]" = Field(
        None,
        description="A Defined Term contained in this term set.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.DefinedTerm import DefinedTerm

    DefinedTermSet.update_forward_refs()
