from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.UKNonprofitType import UKNonprofitType


class CharitableIncorporatedOrganization(UKNonprofitType):
    """CharitableIncorporatedOrganization: Non-profit type referring to a Charitable"
     "Incorporated Organization (UK).

    See: https://schema.org/CharitableIncorporatedOrganization
    Model depth: 6
    """

    type_: str = Field("CharitableIncorporatedOrganization", const=True, alias="@type")


if TYPE_CHECKING:

    CharitableIncorporatedOrganization.update_forward_refs()
