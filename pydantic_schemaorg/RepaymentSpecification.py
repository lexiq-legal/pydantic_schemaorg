from pydantic import Field
from typing import Any, Union, List, Optional
from decimal import Decimal
from pydantic_schemaorg.StructuredValue import StructuredValue


class RepaymentSpecification(StructuredValue):
    """A structured value representing repayment.

    See https://schema.org/RepaymentSpecification.

    """

    loanPaymentAmount: Any = Field(
        None,
        description="The amount of money to pay in a single payment.",
    )
    numberOfLoanPayments: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="The number of payments contractually required at origination to repay the loan. For"
     "monthly paying loans this is the number of months from the contractual first payment"
     "date to the maturity date.",
    )
    loanPaymentFrequency: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="Frequency of payments due, i.e. number of months between payments. This is defined as"
     "a frequency, i.e. the reciprocal of a period of time.",
    )
    earlyPrepaymentPenalty: Any = Field(
        None,
        description="The amount to be paid as a penalty in the event of early payment of the loan.",
    )
    downPayment: Union[List[Union[Decimal, Any]], Union[Decimal, Any]] = Field(
        None,
        description="a type of payment made in cash during the onset of the purchase of an expensive good/service."
     "The payment typically represents only a percentage of the full purchase price.",
    )
    locals().update({"@type": Field("RepaymentSpecification", const=True)})


RepaymentSpecification.update_forward_refs()
