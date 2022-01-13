from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.Intangible import Intangible


class ProgramMembership(Intangible):
    """Used to describe membership in a loyalty programs (e.g. \"StarAliance\"), traveler"
     "clubs (e.g. \"AAA\"), purchase clubs (\"Safeway Club\"), etc.

    See: https://schema.org/ProgramMembership
    Model depth: 3
    """

    type_: str = Field("ProgramMembership", const=True, alias="@type")
    membershipNumber: "Optional[Union[List[str], str]]" = Field(
        None,
        description="A unique identifier for the membership.",
    )
    membershipPointsEarned: "Optional[Union[List[Union[Decimal, QuantitativeValue, str]], Union[Decimal, QuantitativeValue, str]]]" = Field(
        None,
        description="The number of membership points earned by the member. If necessary, the unitText can"
        "be used to express the units the points are issued in. (e.g. stars, miles, etc.)",
    )
    member: "Optional[Union[List[Union[Person, Organization, str]], Union[Person, Organization, str]]]" = Field(
        None,
        description="A member of an Organization or a ProgramMembership. Organizations can be members of"
        "organizations; ProgramMembership is typically for individuals.",
    )
    members: "Optional[Union[List[Union[Person, Organization, str]], Union[Person, Organization, str]]]" = Field(
        None,
        description="A member of this organization.",
    )
    programName: "Optional[Union[List[str], str]]" = Field(
        None,
        description="The program providing the membership.",
    )
    hostingOrganization: "Optional[Union[List[Union[Organization, str]], Union[Organization, str]]]" = Field(
        None,
        description="The organization (airline, travelers' club, etc.) the membership is made with.",
    )


if TYPE_CHECKING:

    from decimal import Decimal

    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue

    from pydantic_schemaorg.Person import Person

    from pydantic_schemaorg.Organization import Organization

    ProgramMembership.update_forward_refs()
