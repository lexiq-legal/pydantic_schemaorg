from pydantic import Field
from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
from pydantic_schemaorg.Place import Place
from typing import Any, Optional, Union, List
from pydantic_schemaorg.DeliveryMethod import DeliveryMethod
from pydantic_schemaorg.PriceSpecification import PriceSpecification


class DeliveryChargeSpecification(PriceSpecification):
    """The price for the delivery of an offer using a particular delivery method.

    See https://schema.org/DeliveryChargeSpecification.

    """
    type_: str = Field("DeliveryChargeSpecification", const=True, alias='@type')
    areaServed: Union[List[Union[str, AdministrativeArea, Place, Any]], Union[str, AdministrativeArea, Place, Any]] = Field(
        None,
        description="The geographic area where a service or offered item is provided.",
    )
    eligibleRegion: Union[List[Union[str, Place, Any]], Union[str, Place, Any]] = Field(
        None,
        description="The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for"
     "the geo-political region(s) for which the offer or delivery charge specification is"
     "valid. See also [[ineligibleRegion]].",
    )
    appliesToDeliveryMethod: Optional[Union[List[DeliveryMethod], DeliveryMethod]] = Field(
        None,
        description="The delivery method(s) to which the delivery charge or payment charge specification"
     "applies.",
    )
    ineligibleRegion: Union[List[Union[str, Place, Any]], Union[str, Place, Any]] = Field(
        None,
        description="The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for"
     "the geo-political region(s) for which the offer or delivery charge specification is"
     "not valid, e.g. a region where the transaction is not allowed. See also [[eligibleRegion]].",
    )
    

DeliveryChargeSpecification.update_forward_refs()
