from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.StructuredValue import StructuredValue


class ContactPoint(StructuredValue):
    """A contact point&#x2014;for example, a Customer Complaints department.

    See: https://schema.org/ContactPoint
    Model depth: 4
    """
    type_: str = Field("ContactPoint", alias='@type')
    areaServed: Optional[Union[List[Union[str, 'Text', 'GeoShape', 'Place', 'AdministrativeArea']], str, 'Text', 'GeoShape', 'Place', 'AdministrativeArea']] = Field(
        None,
        description="The geographic area where a service or offered item is provided.",
    )
    contactType: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="A person or organization can have different contact points, for different purposes."
     "For example, a sales contact point, a PR contact point and so on. This property is used"
     "to specify the kind of contact point.",
    )
    availableLanguage: Optional[Union[List[Union[str, 'Text', 'Language']], str, 'Text', 'Language']] = Field(
        None,
        description="A language someone may use with or at the item, service or place. Please use one of the language"
     "codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also"
     "[[inLanguage]]",
    )
    serviceArea: Optional[Union[List[Union['GeoShape', 'Place', 'AdministrativeArea', str]], 'GeoShape', 'Place', 'AdministrativeArea', str]] = Field(
        None,
        description="The geographic area where the service is provided.",
    )
    email: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Email address.",
    )
    hoursAvailable: Optional[Union[List[Union['OpeningHoursSpecification', str]], 'OpeningHoursSpecification', str]] = Field(
        None,
        description="The hours during which this service or contact is available.",
    )
    telephone: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The telephone number.",
    )
    contactOption: Optional[Union[List[Union['ContactPointOption', str]], 'ContactPointOption', str]] = Field(
        None,
        description="An option available on this contact point (e.g. a toll-free number or support for hearing-impaired"
     "callers).",
    )
    faxNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The fax number.",
    )
    productSupported: Optional[Union[List[Union[str, 'Text', 'Product']], str, 'Text', 'Product']] = Field(
        None,
        description="The product or service this support contact point is related to (such as product support"
     "for a particular product line). This can be a specific product or product line (e.g. \"iPhone\")"
     "or a general category of products or services (e.g. \"smartphones\").",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.GeoShape import GeoShape
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
    from pydantic_schemaorg.Language import Language
    from pydantic_schemaorg.OpeningHoursSpecification import OpeningHoursSpecification
    from pydantic_schemaorg.ContactPointOption import ContactPointOption
    from pydantic_schemaorg.Product import Product
