from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from decimal import Decimal


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class ProgramMembership(Intangible):
    """Used to describe membership in a loyalty programs (e.g. \"StarAliance\"), traveler"
     "clubs (e.g. \"AAA\"), purchase clubs (\"Safeway Club\"), etc.

    See: https://schema.org/ProgramMembership
    Model depth: 3
    """
    type_: str = Field(default="ProgramMembership", alias='@type', constant=True)
    membershipNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A unique identifier for the membership.",
    )
    membershipPointsEarned: Optional[Union[List[Union[int, float, 'Number', 'QuantitativeValue', str]], int, float, 'Number', 'QuantitativeValue', str]] = Field(
        default=None,
        description="The number of membership points earned by the member. If necessary, the unitText can"
     "be used to express the units the points are issued in. (e.g. stars, miles, etc.)",
    )
    member: Optional[Union[List[Union['Organization', 'Person', str]], 'Organization', 'Person', str]] = Field(
        default=None,
        description="A member of an Organization or a ProgramMembership. Organizations can be members of"
     "organizations; ProgramMembership is typically for individuals.",
    )
    members: Optional[Union[List[Union['Organization', 'Person', str]], 'Organization', 'Person', str]] = Field(
        default=None,
        description="A member of this organization.",
    )
    programName: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The program providing the membership.",
    )
    hostingOrganization: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        default=None,
        description="The organization (airline, travelers' club, etc.) the membership is made with.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.Person import Person
