from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from typing import Union, Optional, List
from decimal import Decimal
from pydantic import AnyUrl, StrictBool


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class Order(Intangible):
    """An order is a confirmation of a transaction (a receipt), which can contain multiple line"
     "items, each represented by an Offer that has been accepted by the customer.

    See: https://schema.org/Order
    Model depth: 3
    """
    type_: str = Field("Order", alias='@type')
    orderDate: Optional[Union[List[Union[ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]], ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]] = Field(
        None,
        description="Date order was placed.",
    )
    paymentDue: Optional[Union[List[Union[ISO8601Date, 'DateTime', str]], ISO8601Date, 'DateTime', str]] = Field(
        None,
        description="The date that payment is due.",
    )
    discount: Optional[Union[List[Union[Decimal, 'Number', str, 'Text']], Decimal, 'Number', str, 'Text']] = Field(
        None,
        description="Any discount applied (to an Order).",
    )
    discountCode: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Code used to redeem a discount.",
    )
    paymentMethodId: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="An identifier for the method of payment used (e.g. the last 4 digits of the credit card).",
    )
    orderDelivery: Optional[Union[List[Union['ParcelDelivery', str]], 'ParcelDelivery', str]] = Field(
        None,
        description="The delivery of the parcel related to this order or order item.",
    )
    discountCurrency: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The currency of the discount. Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217)"
     "e.g. \"USD\"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies)"
     "for cryptocurrencies e.g. \"BTC\"; well known names for [Local Exchange Tradings Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)"
     "(LETS) and other currency types e.g. \"Ithaca HOUR\".",
    )
    isGift: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        None,
        description="Was the offer accepted as a gift for someone other than the buyer.",
    )
    orderedItem: Optional[Union[List[Union['Service', 'Product', 'OrderItem', str]], 'Service', 'Product', 'OrderItem', str]] = Field(
        None,
        description="The item ordered.",
    )
    billingAddress: Optional[Union[List[Union['PostalAddress', str]], 'PostalAddress', str]] = Field(
        None,
        description="The billing address for the order.",
    )
    customer: Optional[Union[List[Union['Organization', 'Person', str]], 'Organization', 'Person', str]] = Field(
        None,
        description="Party placing the order or paying the invoice.",
    )
    seller: Optional[Union[List[Union['Organization', 'Person', str]], 'Organization', 'Person', str]] = Field(
        None,
        description="An entity which offers (sells / leases / lends / loans) the services / goods. A seller may"
     "also be a provider.",
    )
    orderStatus: Optional[Union[List[Union['OrderStatus', str]], 'OrderStatus', str]] = Field(
        None,
        description="The current status of the order.",
    )
    partOfInvoice: Optional[Union[List[Union['Invoice', str]], 'Invoice', str]] = Field(
        None,
        description="The order is being paid as part of the referenced Invoice.",
    )
    paymentDueDate: Optional[Union[List[Union[ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]], ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]] = Field(
        None,
        description="The date that payment is due.",
    )
    confirmationNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="A number that confirms the given order or payment has been received.",
    )
    orderNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The identifier of the transaction.",
    )
    acceptedOffer: Optional[Union[List[Union['Offer', str]], 'Offer', str]] = Field(
        None,
        description="The offer(s) -- e.g., product, quantity and price combinations -- included in the order.",
    )
    merchant: Optional[Union[List[Union['Organization', 'Person', str]], 'Organization', 'Person', str]] = Field(
        None,
        description="'merchant' is an out-dated term for 'seller'.",
    )
    paymentUrl: Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]] = Field(
        None,
        description="The URL for sending a payment.",
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
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.ParcelDelivery import ParcelDelivery
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.Service import Service
    from pydantic_schemaorg.Product import Product
    from pydantic_schemaorg.OrderItem import OrderItem
    from pydantic_schemaorg.PostalAddress import PostalAddress
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.OrderStatus import OrderStatus
    from pydantic_schemaorg.Invoice import Invoice
    from pydantic_schemaorg.Offer import Offer
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.PaymentMethod import PaymentMethod
