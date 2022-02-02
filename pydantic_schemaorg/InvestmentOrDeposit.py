from __future__ import annotations
from typing import TYPE_CHECKING

from decimal import Decimal
from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.FinancialProduct import FinancialProduct


class InvestmentOrDeposit(FinancialProduct):
    """A type of financial product that typically requires the client to transfer funds to a"
     "financial service in return for potential beneficial financial return.

    See: https://schema.org/InvestmentOrDeposit
    Model depth: 5
    """
    type_: str = Field("InvestmentOrDeposit", alias='@type')
    amount: Optional[Union[List[Union[Decimal, 'Number', 'MonetaryAmount', str]], Decimal, 'Number', 'MonetaryAmount', str]] = Field(
        None,
        description="The amount of money.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.MonetaryAmount import MonetaryAmount
