from pydantic import Field
from decimal import Decimal
from typing import Any, Union, List, Optional
from pydantic_schemaorg.FinancialProduct import FinancialProduct


class InvestmentOrDeposit(FinancialProduct):
    """A type of financial product that typically requires the client to transfer funds to a"
     "financial service in return for potential beneficial financial return.

    See https://schema.org/InvestmentOrDeposit.

    """

    amount: Union[List[Union[Decimal, Any]], Union[Decimal, Any]] = Field(
        None,
        description="The amount of money.",
    )
    locals().update({"@type": Field("InvestmentOrDeposit", const=True)})


InvestmentOrDeposit.update_forward_refs()
