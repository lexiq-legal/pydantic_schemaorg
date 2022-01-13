from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.LoanOrCredit import LoanOrCredit


class MortgageLoan(LoanOrCredit):
    """A loan in which property or real estate is used as collateral. (A loan securitized against"
     "some real estate).

    See: https://schema.org/MortgageLoan
    Model depth: 6
    """

    type_: str = Field("MortgageLoan", const=True, alias="@type")
    domiciledMortgage: "Optional[Union[List[Union[StrictBool, str]], Union[StrictBool, str]]]" = Field(
        None,
        description="Whether borrower is a resident of the jurisdiction where the property is located.",
    )
    loanMortgageMandateAmount: "Optional[Union[List[Union[MonetaryAmount, str]], Union[MonetaryAmount, str]]]" = Field(
        None,
        description="Amount of mortgage mandate that can be converted into a proper mortgage at a later stage.",
    )


if TYPE_CHECKING:

    from pydantic import StrictBool

    from pydantic_schemaorg.MonetaryAmount import MonetaryAmount

    MortgageLoan.update_forward_refs()
