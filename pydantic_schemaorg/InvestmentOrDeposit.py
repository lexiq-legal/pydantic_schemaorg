from pydantic import Field
from decimal import Decimal
from pydantic_schemaorg.MonetaryAmount import MonetaryAmount
from typing import List, Optional, Union
from pydantic_schemaorg.FinancialProduct import FinancialProduct


class InvestmentOrDeposit(FinancialProduct):
    """A type of financial product that typically requires the client to transfer funds to a"
     "financial service in return for potential beneficial financial return.

    See https://schema.org/InvestmentOrDeposit.

    """
    type_: str = Field("InvestmentOrDeposit", const=True, alias='@type')
    amount: Optional[Union[List[Union[Decimal, MonetaryAmount, str]], Union[Decimal, MonetaryAmount, str]]] = Field(
        None,
        description="The amount of money.",
    )
    

InvestmentOrDeposit.update_forward_refs()
