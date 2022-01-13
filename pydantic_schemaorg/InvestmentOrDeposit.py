from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.FinancialProduct import FinancialProduct


class InvestmentOrDeposit(FinancialProduct):
    """A type of financial product that typically requires the client to transfer funds to a"
     "financial service in return for potential beneficial financial return.

    See: https://schema.org/InvestmentOrDeposit
    Model depth: 5
    """

    type_: str = Field("InvestmentOrDeposit", const=True, alias="@type")
    amount: "Optional[Union[List[Union[Decimal, MonetaryAmount, str]], Union[Decimal, MonetaryAmount, str]]]" = Field(
        None,
        description="The amount of money.",
    )


if TYPE_CHECKING:

    from decimal import Decimal

    from pydantic_schemaorg.MonetaryAmount import MonetaryAmount

    InvestmentOrDeposit.update_forward_refs()
