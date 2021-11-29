from pydantic import Field, StrictBool
from typing import Any, Union, List, Optional
from pydantic_schemaorg.LoanOrCredit import LoanOrCredit


class MortgageLoan(LoanOrCredit):
    """A loan in which property or real estate is used as collateral. (A loan securitized against"
     "some real estate).

    See https://schema.org/MortgageLoan.

    """

    domiciledMortgage: Optional[Union[List[StrictBool], StrictBool]] = Field(
        None,
        description="Whether borrower is a resident of the jurisdiction where the property is located.",
    )
    loanMortgageMandateAmount: Any = Field(
        None,
        description="Amount of mortgage mandate that can be converted into a proper mortgage at a later stage.",
    )
    locals().update({"@type": Field("MortgageLoan", const=True)})


MortgageLoan.update_forward_refs()
