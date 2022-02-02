from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from pydantic import AnyUrl
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class ParcelDelivery(Intangible):
    """The delivery of a parcel either via the postal service or a commercial service.

    See: https://schema.org/ParcelDelivery
    Model depth: 3
    """
    type_: str = Field("ParcelDelivery", alias='@type')
    trackingNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Shipper tracking number.",
    )
    itemShipped: Optional[Union[List[Union['Product', str]], 'Product', str]] = Field(
        None,
        description="Item(s) being shipped.",
    )
    trackingUrl: Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]] = Field(
        None,
        description="Tracking url for the parcel delivery.",
    )
    expectedArrivalFrom: Optional[Union[List[Union[ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]], ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]] = Field(
        None,
        description="The earliest date the package may arrive.",
    )
    expectedArrivalUntil: Optional[Union[List[Union[ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]], ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]] = Field(
        None,
        description="The latest date the package may arrive.",
    )
    deliveryAddress: Optional[Union[List[Union['PostalAddress', str]], 'PostalAddress', str]] = Field(
        None,
        description="Destination address.",
    )
    hasDeliveryMethod: Optional[Union[List[Union['DeliveryMethod', str]], 'DeliveryMethod', str]] = Field(
        None,
        description="Method used for delivery or shipping.",
    )
    carrier: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        None,
        description="'carrier' is an out-dated term indicating the 'provider' for parcel delivery and flights.",
    )
    originAddress: Optional[Union[List[Union['PostalAddress', str]], 'PostalAddress', str]] = Field(
        None,
        description="Shipper's address.",
    )
    provider: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",
    )
    deliveryStatus: Optional[Union[List[Union['DeliveryEvent', str]], 'DeliveryEvent', str]] = Field(
        None,
        description="New entry added as the package passes through each leg of its journey (from shipment to"
     "final delivery).",
    )
    partOfOrder: Optional[Union[List[Union['Order', str]], 'Order', str]] = Field(
        None,
        description="The overall order the items in this delivery were included in.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Product import Product
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.PostalAddress import PostalAddress
    from pydantic_schemaorg.DeliveryMethod import DeliveryMethod
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.DeliveryEvent import DeliveryEvent
    from pydantic_schemaorg.Order import Order
