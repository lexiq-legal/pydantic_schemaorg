from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.FinancialService import FinancialService


class BankOrCreditUnion(FinancialService):
    """Bank or credit union.

    See: https://schema.org/BankOrCreditUnion
    Model depth: 5
    """

    type_: str = Field("BankOrCreditUnion", const=True, alias="@type")


if TYPE_CHECKING:

    BankOrCreditUnion.update_forward_refs()
