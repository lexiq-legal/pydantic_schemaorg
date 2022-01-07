from pydantic import Field
from pydantic_schemaorg.MonetaryAmount import MonetaryAmount
from typing import List, Optional, Union
from decimal import Decimal
from pydantic_schemaorg.StructuredValue import StructuredValue


class RepaymentSpecification(StructuredValue):
    """A structured value representing repayment.

    See https://schema.org/RepaymentSpecification.

    """
    type_: str = Field("RepaymentSpecification", const=True, alias='@type')
    loanPaymentAmount: Optional[Union[List[Union[MonetaryAmount, str]], Union[MonetaryAmount, str]]] = Field(
        None,
        description="The amount of money to pay in a single payment.",
    )
    numberOfLoanPayments: Optional[Union[List[Union[Decimal, str]], Union[Decimal, str]]] = Field(
        None,
        description="The number of payments contractually required at origination to repay the loan. For"
     "monthly paying loans this is the number of months from the contractual first payment"
     "date to the maturity date.",
    )
    loanPaymentFrequency: Optional[Union[List[Union[Decimal, str]], Union[Decimal, str]]] = Field(
        None,
        description="Frequency of payments due, i.e. number of months between payments. This is defined as"
     "a frequency, i.e. the reciprocal of a period of time.",
    )
    earlyPrepaymentPenalty: Optional[Union[List[Union[MonetaryAmount, str]], Union[MonetaryAmount, str]]] = Field(
        None,
        description="The amount to be paid as a penalty in the event of early payment of the loan.",
    )
    downPayment: Optional[Union[List[Union[Decimal, MonetaryAmount, str]], Union[Decimal, MonetaryAmount, str]]] = Field(
        None,
        description="a type of payment made in cash during the onset of the purchase of an expensive good/service."
     "The payment typically represents only a percentage of the full purchase price.",
    )
    

RepaymentSpecification.update_forward_refs()
