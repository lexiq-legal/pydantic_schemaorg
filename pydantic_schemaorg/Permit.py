from pydantic import Field
from typing import Any, Union, List, Optional
from datetime import date, datetime
from pydantic_schemaorg.Audience import Audience
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Intangible import Intangible


class Permit(Intangible):
    """A permit issued by an organization, e.g. a parking pass.

    See https://schema.org/Permit.

    """

    issuedThrough: Any = Field(
        None,
        description="The service through with the permit was granted.",
    )
    validFor: Any = Field(
        None,
        description="The duration of validity of a permit or similar thing.",
    )
    validUntil: Optional[Union[List[date], date]] = Field(
        None,
        description="The date when the item is no longer valid.",
    )
    validFrom: Optional[Union[List[Union[datetime, date]], Union[datetime, date]]] = Field(
        None,
        description="The date when the item becomes valid.",
    )
    permitAudience: Optional[Union[List[Audience], Audience]] = Field(
        None,
        description="The target audience for this permit.",
    )
    issuedBy: Optional[Union[List[Organization], Organization]] = Field(
        None,
        description="The organization issuing the ticket or permit.",
    )
    validIn: Any = Field(
        None,
        description="The geographic area where a permit or similar thing is valid.",
    )
    locals().update({"@type": Field("Permit", const=True)})


Permit.update_forward_refs()
