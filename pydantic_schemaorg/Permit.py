from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.Intangible import Intangible


class Permit(Intangible):
    """A permit issued by an organization, e.g. a parking pass.

    See: https://schema.org/Permit
    Model depth: 3
    """

    type_: str = Field("Permit", const=True, alias="@type")
    issuedThrough: "Optional[Union[List[Union[Service, str]], Union[Service, str]]]" = (
        Field(
            None,
            description="The service through with the permit was granted.",
        )
    )
    validFor: "Optional[Union[List[Union[Duration, str]], Union[Duration, str]]]" = (
        Field(
            None,
            description="The duration of validity of a permit or similar thing.",
        )
    )
    validUntil: "Optional[Union[List[Union[date, str]], Union[date, str]]]" = Field(
        None,
        description="The date when the item is no longer valid.",
    )
    validFrom: "Optional[Union[List[Union[datetime, date, str]], Union[datetime, date, str]]]" = Field(
        None,
        description="The date when the item becomes valid.",
    )
    permitAudience: "Optional[Union[List[Union[Audience, str]], Union[Audience, str]]]" = Field(
        None,
        description="The target audience for this permit.",
    )
    issuedBy: "Optional[Union[List[Union[Organization, str]], Union[Organization, str]]]" = Field(
        None,
        description="The organization issuing the ticket or permit.",
    )
    validIn: "Optional[Union[List[Union[AdministrativeArea, str]], Union[AdministrativeArea, str]]]" = Field(
        None,
        description="The geographic area where a permit or similar thing is valid.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.Service import Service

    from pydantic_schemaorg.Duration import Duration

    from datetime import date, datetime

    from pydantic_schemaorg.Audience import Audience

    from pydantic_schemaorg.Organization import Organization

    from pydantic_schemaorg.AdministrativeArea import AdministrativeArea

    Permit.update_forward_refs()
