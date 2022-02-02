from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class Permit(Intangible):
    """A permit issued by an organization, e.g. a parking pass.

    See: https://schema.org/Permit
    Model depth: 3
    """
    type_: str = Field("Permit", alias='@type')
    issuedThrough: Optional[Union[List[Union['Service', str]], 'Service', str]] = Field(
        None,
        description="The service through with the permit was granted.",
    )
    validFor: Optional[Union[List[Union['Duration', str]], 'Duration', str]] = Field(
        None,
        description="The duration of validity of a permit or similar thing.",
    )
    validUntil: Optional[Union[List[Union[ISO8601Date, 'Date', str]], ISO8601Date, 'Date', str]] = Field(
        None,
        description="The date when the item is no longer valid.",
    )
    validFrom: Optional[Union[List[Union[ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]], ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]] = Field(
        None,
        description="The date when the item becomes valid.",
    )
    permitAudience: Optional[Union[List[Union['Audience', str]], 'Audience', str]] = Field(
        None,
        description="The target audience for this permit.",
    )
    issuedBy: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        None,
        description="The organization issuing the ticket or permit.",
    )
    validIn: Optional[Union[List[Union['AdministrativeArea', str]], 'AdministrativeArea', str]] = Field(
        None,
        description="The geographic area where a permit or similar thing is valid.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Service import Service
    from pydantic_schemaorg.Duration import Duration
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Audience import Audience
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
