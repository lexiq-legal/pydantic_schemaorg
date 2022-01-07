from pydantic import StrictBool, Field
from typing import List, Optional, Union
from pydantic_schemaorg.MonetaryAmount import MonetaryAmount
from pydantic_schemaorg.LoanOrCredit import LoanOrCredit


class MortgageLoan(LoanOrCredit):
    """A loan in which property or real estate is used as collateral. (A loan securitized against"
     "some real estate).

    See https://schema.org/MortgageLoan.

    """
    type_: str = Field("MortgageLoan", const=True, alias='@type')
    domiciledMortgage: Optional[Union[List[Union[StrictBool, str]], Union[StrictBool, str]]] = Field(
        None,
        description="Whether borrower is a resident of the jurisdiction where the property is located.",
    )
    loanMortgageMandateAmount: Optional[Union[List[Union[MonetaryAmount, str]], Union[MonetaryAmount, str]]] = Field(
        None,
        description="Amount of mortgage mandate that can be converted into a proper mortgage at a later stage.",
    )
    

MortgageLoan.update_forward_refs()
