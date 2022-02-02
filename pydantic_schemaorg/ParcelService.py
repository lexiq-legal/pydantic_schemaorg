from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.DeliveryMethod import DeliveryMethod


class ParcelService(DeliveryMethod):
    """A private parcel service as the delivery mode available for a certain offer. Commonly"
     "used values: * http://purl.org/goodrelations/v1#DHL * http://purl.org/goodrelations/v1#FederalExpress"
     "* http://purl.org/goodrelations/v1#UPS

    See: https://schema.org/ParcelService
    Model depth: 5
    """
    type_: str = Field("ParcelService", alias='@type')
    

