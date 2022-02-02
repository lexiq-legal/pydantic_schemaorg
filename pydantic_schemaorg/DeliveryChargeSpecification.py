from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.PriceSpecification import PriceSpecification


class DeliveryChargeSpecification(PriceSpecification):
    """The price for the delivery of an offer using a particular delivery method.

    See: https://schema.org/DeliveryChargeSpecification
    Model depth: 5
    """
    type_: str = Field("DeliveryChargeSpecification", alias='@type')
    areaServed: Optional[Union[List[Union[str, 'Text', 'GeoShape', 'Place', 'AdministrativeArea']], str, 'Text', 'GeoShape', 'Place', 'AdministrativeArea']] = Field(
        None,
        description="The geographic area where a service or offered item is provided.",
    )
    eligibleRegion: Optional[Union[List[Union[str, 'Text', 'GeoShape', 'Place']], str, 'Text', 'GeoShape', 'Place']] = Field(
        None,
        description="The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for"
     "the geo-political region(s) for which the offer or delivery charge specification is"
     "valid. See also [[ineligibleRegion]].",
    )
    appliesToDeliveryMethod: Optional[Union[List[Union['DeliveryMethod', str]], 'DeliveryMethod', str]] = Field(
        None,
        description="The delivery method(s) to which the delivery charge or payment charge specification"
     "applies.",
    )
    ineligibleRegion: Optional[Union[List[Union[str, 'Text', 'GeoShape', 'Place']], str, 'Text', 'GeoShape', 'Place']] = Field(
        None,
        description="The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for"
     "the geo-political region(s) for which the offer or delivery charge specification is"
     "not valid, e.g. a region where the transaction is not allowed. See also [[eligibleRegion]].",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.GeoShape import GeoShape
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
    from pydantic_schemaorg.DeliveryMethod import DeliveryMethod
