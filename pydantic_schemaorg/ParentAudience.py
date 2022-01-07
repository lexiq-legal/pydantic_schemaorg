from pydantic import Field
from decimal import Decimal
from typing import List, Optional, Union
from pydantic_schemaorg.PeopleAudience import PeopleAudience


class ParentAudience(PeopleAudience):
    """A set of characteristics describing parents, who can be interested in viewing some content.

    See https://schema.org/ParentAudience.

    """
    type_: str = Field("ParentAudience", const=True, alias='@type')
    childMinAge: Optional[Union[List[Union[Decimal, str]], Union[Decimal, str]]] = Field(
        None,
        description="Minimal age of the child.",
    )
    childMaxAge: Optional[Union[List[Union[Decimal, str]], Union[Decimal, str]]] = Field(
        None,
        description="Maximal age of the child.",
    )
    

ParentAudience.update_forward_refs()
