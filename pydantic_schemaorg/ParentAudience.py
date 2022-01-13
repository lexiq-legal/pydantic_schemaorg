from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.PeopleAudience import PeopleAudience


class ParentAudience(PeopleAudience):
    """A set of characteristics describing parents, who can be interested in viewing some content.

    See: https://schema.org/ParentAudience
    Model depth: 5
    """

    type_: str = Field("ParentAudience", const=True, alias="@type")
    childMinAge: "Optional[Union[List[Union[Decimal, str]], Union[Decimal, str]]]" = (
        Field(
            None,
            description="Minimal age of the child.",
        )
    )
    childMaxAge: "Optional[Union[List[Union[Decimal, str]], Union[Decimal, str]]]" = (
        Field(
            None,
            description="Maximal age of the child.",
        )
    )


if TYPE_CHECKING:

    from decimal import Decimal

    ParentAudience.update_forward_refs()
