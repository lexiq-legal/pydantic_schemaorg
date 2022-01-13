from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c4(USNonprofitType):
    """Nonprofit501c4: Non-profit type referring to Civic Leagues, Social Welfare Organizations,"
     "and Local Associations of Employees.

    See: https://schema.org/Nonprofit501c4
    Model depth: 6
    """

    type_: str = Field("Nonprofit501c4", const=True, alias="@type")


if TYPE_CHECKING:

    Nonprofit501c4.update_forward_refs()
