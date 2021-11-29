from pydantic import Field, AnyUrl
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Product import Product
from datetime import date, datetime
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

    trackingNumber: Optional[Union[List[str], str]] = Field(
        None,
        description="Shipper tracking number.",
    )
    itemShipped: Optional[Union[List[Product], Product]] = Field(
        None,
        description="Item(s) being shipped.",
    )
    trackingUrl: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None,
        description="Tracking url for the parcel delivery.",
    )
    expectedArrivalFrom: Optional[Union[List[Union[datetime, date]], Union[datetime, date]]] = Field(
        None,
        description="The earliest date the package may arrive.",
    )
    expectedArrivalUntil: Optional[Union[List[Union[datetime, date]], Union[datetime, date]]] = Field(
        None,
        description="The latest date the package may arrive.",
    )
    deliveryAddress: Optional[Union[List[PostalAddress], PostalAddress]] = Field(
        None,
        description="Destination address.",
    )
    hasDeliveryMethod: Optional[Union[List[DeliveryMethod], DeliveryMethod]] = Field(
        None,
        description="Method used for delivery or shipping.",
    )
    carrier: Optional[Union[List[Organization], Organization]] = Field(
        None,
        description="'carrier' is an out-dated term indicating the 'provider' for parcel delivery and flights.",
    )
    originAddress: Optional[Union[List[PostalAddress], PostalAddress]] = Field(
        None,
        description="Shipper's address.",
    )
    provider: Optional[Union[List[Union[Organization, Person]], Union[Organization, Person]]] = Field(
        None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",
    )
    deliveryStatus: Optional[Union[List[DeliveryEvent], DeliveryEvent]] = Field(
        None,
        description="New entry added as the package passes through each leg of its journey (from shipment to"
     "final delivery).",
    )
    partOfOrder: Optional[Union[List[Order], Order]] = Field(
        None,
        description="The overall order the items in this delivery were included in.",
    )
    locals().update({"@type": Field("ParcelDelivery", const=True)})


ParcelDelivery.update_forward_refs()
