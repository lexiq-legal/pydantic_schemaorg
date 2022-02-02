from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic import StrictBool
from typing import Union, Optional, List
from decimal import Decimal


from pydantic import Field
from pydantic_schemaorg.PaymentMethod import PaymentMethod
from pydantic_schemaorg.FinancialProduct import FinancialProduct


class PaymentCard(PaymentMethod, FinancialProduct):
    """A payment method using a credit, debit, store or other card to associate the payment with"
     "an account.

    See: https://schema.org/PaymentCard
    Model depth: 5
    """
    type_: str = Field("PaymentCard", alias='@type')
    contactlessPayment: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        None,
        description="A secure method for consumers to purchase products or services via debit, credit or smartcards"
     "by using RFID or NFC technology.",
    )
    cashBack: Optional[Union[List[Union[Decimal, 'Number', StrictBool, 'Boolean', str]], Decimal, 'Number', StrictBool, 'Boolean', str]] = Field(
        None,
        description="A cardholder benefit that pays the cardholder a small percentage of their net expenditures.",
    )
    floorLimit: Optional[Union[List[Union['MonetaryAmount', str]], 'MonetaryAmount', str]] = Field(
        None,
        description="A floor limit is the amount of money above which credit card transactions must be authorized.",
    )
    monthlyMinimumRepaymentAmount: Optional[Union[List[Union[Decimal, 'Number', 'MonetaryAmount', str]], Decimal, 'Number', 'MonetaryAmount', str]] = Field(
        None,
        description="The minimum payment is the lowest amount of money that one is required to pay on a credit"
     "card statement each month.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.MonetaryAmount import MonetaryAmount
