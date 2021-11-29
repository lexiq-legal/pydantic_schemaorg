from pydantic import Field, AnyUrl
from datetime import date, datetime
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Duration import Duration
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory
from pydantic_schemaorg.PaymentStatusType import PaymentStatusType
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.PriceSpecification import PriceSpecification
from pydantic_schemaorg.Order import Order
from pydantic_schemaorg.PaymentMethod import PaymentMethod
from pydantic_schemaorg.Intangible import Intangible


class Invoice(Intangible):
    """A statement of the money due for goods or services; a bill.

    See https://schema.org/Invoice.

    """

    paymentDue: Optional[Union[List[datetime], datetime]] = Field(
        None,
        description="The date that payment is due.",
    )
    paymentMethodId: Optional[Union[List[str], str]] = Field(
        None,
        description="An identifier for the method of payment used (e.g. the last 4 digits of the credit card).",
    )
    accountId: Optional[Union[List[str], str]] = Field(
        None,
        description="The identifier for the account the payment will be applied to.",
    )
    billingPeriod: Optional[Union[List[Duration], Duration]] = Field(
        None,
        description="The time interval used to compute the invoice.",
    )
    category: Optional[Union[List[Union[AnyUrl, str, Thing, PhysicalActivityCategory]], Union[AnyUrl, str, Thing, PhysicalActivityCategory]]] = Field(
        None,
        description="A category for the item. Greater signs or slashes can be used to informally indicate a"
     "category hierarchy.",
    )
    paymentStatus: Optional[Union[List[Union[str, PaymentStatusType]], Union[str, PaymentStatusType]]] = Field(
        None,
        description="The status of payment; whether the invoice has been paid or not.",
    )
    customer: Optional[Union[List[Union[Organization, Person]], Union[Organization, Person]]] = Field(
        None,
        description="Party placing the order or paying the invoice.",
    )
    totalPaymentDue: Union[List[Union[PriceSpecification, Any]], Union[PriceSpecification, Any]] = Field(
        None,
        description="The total amount due.",
    )
    paymentDueDate: Optional[Union[List[Union[datetime, date]], Union[datetime, date]]] = Field(
        None,
        description="The date that payment is due.",
    )
    scheduledPaymentDate: Optional[Union[List[date], date]] = Field(
        None,
        description="The date the invoice is scheduled to be paid.",
    )
    referencesOrder: Optional[Union[List[Order], Order]] = Field(
        None,
        description="The Order(s) related to this Invoice. One or more Orders may be combined into a single"
     "Invoice.",
    )
    confirmationNumber: Optional[Union[List[str], str]] = Field(
        None,
        description="A number that confirms the given order or payment has been received.",
    )
    minimumPaymentDue: Union[List[Union[PriceSpecification, Any]], Union[PriceSpecification, Any]] = Field(
        None,
        description="The minimum payment required at this time.",
    )
    provider: Optional[Union[List[Union[Organization, Person]], Union[Organization, Person]]] = Field(
        None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",
    )
    paymentMethod: Optional[Union[List[PaymentMethod], PaymentMethod]] = Field(
        None,
        description="The name of the credit card or other method of payment for the order.",
    )
    broker: Optional[Union[List[Union[Organization, Person]], Union[Organization, Person]]] = Field(
        None,
        description="An entity that arranges for an exchange between a buyer and a seller. In most cases a broker"
     "never acquires or releases ownership of a product or service involved in an exchange."
     "If it is not clear whether an entity is a broker, seller, or buyer, the latter two terms"
     "are preferred.",
    )
    locals().update({"@type": Field("Invoice", const=True)})


Invoice.update_forward_refs()
