from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.FinancialService import FinancialService


class InsuranceAgency(FinancialService):
    """An Insurance agency.

    See: https://schema.org/InsuranceAgency
    Model depth: 5
    """

    type_: str = Field("InsuranceAgency", const=True, alias="@type")


if TYPE_CHECKING:

    InsuranceAgency.update_forward_refs()
