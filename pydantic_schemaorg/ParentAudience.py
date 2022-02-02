from __future__ import annotations
from typing import TYPE_CHECKING

from decimal import Decimal
from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.PeopleAudience import PeopleAudience


class ParentAudience(PeopleAudience):
    """A set of characteristics describing parents, who can be interested in viewing some content.

    See: https://schema.org/ParentAudience
    Model depth: 5
    """
    type_: str = Field("ParentAudience", alias='@type')
    childMinAge: Optional[Union[List[Union[Decimal, 'Number', str]], Decimal, 'Number', str]] = Field(
        None,
        description="Minimal age of the child.",
    )
    childMaxAge: Optional[Union[List[Union[Decimal, 'Number', str]], Decimal, 'Number', str]] = Field(
        None,
        description="Maximal age of the child.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
