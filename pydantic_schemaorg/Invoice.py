from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from typing import Union, Optional, List
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class Invoice(Intangible):
    """A statement of the money due for goods or services; a bill.

    See: https://schema.org/Invoice
    Model depth: 3
    """
    type_: str = Field("Invoice", alias='@type')
    paymentDue: Optional[Union[List[Union[ISO8601Date, 'DateTime', str]], ISO8601Date, 'DateTime', str]] = Field(
        None,
        description="The date that payment is due.",
    )
    paymentMethodId: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="An identifier for the method of payment used (e.g. the last 4 digits of the credit card).",
    )
    accountId: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The identifier for the account the payment will be applied to.",
    )
    billingPeriod: Optional[Union[List[Union['Duration', str]], 'Duration', str]] = Field(
        None,
        description="The time interval used to compute the invoice.",
    )
    category: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'Thing', 'PhysicalActivityCategory']], AnyUrl, 'URL', str, 'Text', 'Thing', 'PhysicalActivityCategory']] = Field(
        None,
        description="A category for the item. Greater signs or slashes can be used to informally indicate a"
     "category hierarchy.",
    )
    paymentStatus: Optional[Union[List[Union[str, 'Text', 'PaymentStatusType']], str, 'Text', 'PaymentStatusType']] = Field(
        None,
        description="The status of payment; whether the invoice has been paid or not.",
    )
    customer: Optional[Union[List[Union['Organization', 'Person', str]], 'Organization', 'Person', str]] = Field(
        None,
        description="Party placing the order or paying the invoice.",
    )
    totalPaymentDue: Optional[Union[List[Union['PriceSpecification', 'MonetaryAmount', str]], 'PriceSpecification', 'MonetaryAmount', str]] = Field(
        None,
        description="The total amount due.",
    )
    paymentDueDate: Optional[Union[List[Union[ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]], ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]] = Field(
        None,
        description="The date that payment is due.",
    )
    scheduledPaymentDate: Optional[Union[List[Union[ISO8601Date, 'Date', str]], ISO8601Date, 'Date', str]] = Field(
        None,
        description="The date the invoice is scheduled to be paid.",
    )
    referencesOrder: Optional[Union[List[Union['Order', str]], 'Order', str]] = Field(
        None,
        description="The Order(s) related to this Invoice. One or more Orders may be combined into a single"
     "Invoice.",
    )
    confirmationNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="A number that confirms the given order or payment has been received.",
    )
    minimumPaymentDue: Optional[Union[List[Union['PriceSpecification', 'MonetaryAmount', str]], 'PriceSpecification', 'MonetaryAmount', str]] = Field(
        None,
        description="The minimum payment required at this time.",
    )
    provider: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",
    )
    paymentMethod: Optional[Union[List[Union['PaymentMethod', str]], 'PaymentMethod', str]] = Field(
        None,
        description="The name of the credit card or other method of payment for the order.",
    )
    broker: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        None,
        description="An entity that arranges for an exchange between a buyer and a seller. In most cases a broker"
     "never acquires or releases ownership of a product or service involved in an exchange."
     "If it is not clear whether an entity is a broker, seller, or buyer, the latter two terms"
     "are preferred.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Duration import Duration
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory
    from pydantic_schemaorg.PaymentStatusType import PaymentStatusType
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.PriceSpecification import PriceSpecification
    from pydantic_schemaorg.MonetaryAmount import MonetaryAmount
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.Order import Order
    from pydantic_schemaorg.PaymentMethod import PaymentMethod
