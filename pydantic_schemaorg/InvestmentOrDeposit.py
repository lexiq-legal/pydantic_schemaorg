from pydantic import Field
from decimal import Decimal
from typing import Any, Optional, Union, List
from pydantic_schemaorg.FinancialProduct import FinancialProduct


class InvestmentOrDeposit(FinancialProduct):
    """A type of financial product that typically requires the client to transfer funds to a"
     "financial service in return for potential beneficial financial return.

    See https://schema.org/InvestmentOrDeposit.

    """
    type_: str = Field("InvestmentOrDeposit", const=True, alias='@type')
    amount: Union[List[Union[Decimal, Any]], Union[Decimal, Any]] = Field(
        None,
        description="The amount of money.",
    )
    

InvestmentOrDeposit.update_forward_refs()
