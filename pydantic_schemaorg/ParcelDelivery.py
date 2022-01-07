from pydantic import AnyUrl, Field
from typing import List, Optional, Union
from pydantic_schemaorg.Product import Product
from datetime import datetime, date
from pydantic_schemaorg.PostalAddress import PostalAddress
from pydantic_schemaorg.DeliveryMethod import DeliveryMethod
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.DeliveryEvent import DeliveryEvent
from pydantic_schemaorg.Order import Order
from pydantic_schemaorg.Intangible import Intangible


class ParcelDelivery(Intangible):
    """The delivery of a parcel either via the postal service or a commercial service.

    See https://schema.org/ParcelDelivery.

    """
    type_: str = Field("ParcelDelivery", const=True, alias='@type')
    trackingNumber: Optional[Union[List[str], str]] = Field(
        None,
        description="Shipper tracking number.",
    )
    itemShipped: Optional[Union[List[Union[Product, str]], Union[Product, str]]] = Field(
        None,
        description="Item(s) being shipped.",
    )
    trackingUrl: Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]] = Field(
        None,
        description="Tracking url for the parcel delivery.",
    )
    expectedArrivalFrom: Optional[Union[List[Union[datetime, date, str]], Union[datetime, date, str]]] = Field(
        None,
        description="The earliest date the package may arrive.",
    )
    expectedArrivalUntil: Optional[Union[List[Union[datetime, date, str]], Union[datetime, date, str]]] = Field(
        None,
        description="The latest date the package may arrive.",
    )
    deliveryAddress: Optional[Union[List[Union[PostalAddress, str]], Union[PostalAddress, str]]] = Field(
        None,
        description="Destination address.",
    )
    hasDeliveryMethod: Optional[Union[List[Union[DeliveryMethod, str]], Union[DeliveryMethod, str]]] = Field(
        None,
        description="Method used for delivery or shipping.",
    )
    carrier: Optional[Union[List[Union[Organization, str]], Union[Organization, str]]] = Field(
        None,
        description="'carrier' is an out-dated term indicating the 'provider' for parcel delivery and flights.",
    )
    originAddress: Optional[Union[List[Union[PostalAddress, str]], Union[PostalAddress, str]]] = Field(
        None,
        description="Shipper's address.",
    )
    provider: Optional[Union[List[Union[Organization, Person, str]], Union[Organization, Person, str]]] = Field(
        None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",
    )
    deliveryStatus: Optional[Union[List[Union[DeliveryEvent, str]], Union[DeliveryEvent, str]]] = Field(
        None,
        description="New entry added as the package passes through each leg of its journey (from shipment to"
     "final delivery).",
    )
    partOfOrder: Optional[Union[List[Union[Order, str]], Union[Order, str]]] = Field(
        None,
        description="The overall order the items in this delivery were included in.",
    )
    

ParcelDelivery.update_forward_refs()
