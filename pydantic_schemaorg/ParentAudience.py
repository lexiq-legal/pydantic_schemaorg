from pydantic import Field
from decimal import Decimal
from typing import Any, Union, List, Optional
from pydantic_schemaorg.PeopleAudience import PeopleAudience


class ParentAudience(PeopleAudience):
    """A set of characteristics describing parents, who can be interested in viewing some content.

    See https://schema.org/ParentAudience.

    """

    childMinAge: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="Minimal age of the child.",
    )
    childMaxAge: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="Maximal age of the child.",
    )
    locals().update({"@type": Field("ParentAudience", const=True)})


ParentAudience.update_forward_refs()
