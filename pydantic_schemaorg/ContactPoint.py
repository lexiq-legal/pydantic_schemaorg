from pydantic import Field
from pydantic_schemaorg.Place import Place
from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
from typing import Any, Union, List, Optional
from pydantic_schemaorg.ContactPointOption import ContactPointOption
from pydantic_schemaorg.Product import Product
from pydantic_schemaorg.StructuredValue import StructuredValue


class ContactPoint(StructuredValue):
    """A contact point&#x2014;for example, a Customer Complaints department.

    See https://schema.org/ContactPoint.

    """

    areaServed: Union[List[Union[str, Place, AdministrativeArea, Any]], Union[str, Place, AdministrativeArea, Any]] = Field(
        None,
        description="The geographic area where a service or offered item is provided.",
    )
    contactType: Optional[Union[List[str], str]] = Field(
        None,
        description="A person or organization can have different contact points, for different purposes."
     "For example, a sales contact point, a PR contact point and so on. This property is used"
     "to specify the kind of contact point.",
    )
    availableLanguage: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="A language someone may use with or at the item, service or place. Please use one of the language"
     "codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also"
     "[[inLanguage]]",
    )
    serviceArea: Union[List[Union[AdministrativeArea, Place, Any]], Union[AdministrativeArea, Place, Any]] = Field(
        None,
        description="The geographic area where the service is provided.",
    )
    email: Optional[Union[List[str], str]] = Field(
        None,
        description="Email address.",
    )
    hoursAvailable: Any = Field(
        None,
        description="The hours during which this service or contact is available.",
    )
    telephone: Optional[Union[List[str], str]] = Field(
        None,
        description="The telephone number.",
    )
    contactOption: Optional[Union[List[ContactPointOption], ContactPointOption]] = Field(
        None,
        description="An option available on this contact point (e.g. a toll-free number or support for hearing-impaired"
     "callers).",
    )
    faxNumber: Optional[Union[List[str], str]] = Field(
        None,
        description="The fax number.",
    )
    productSupported: Optional[Union[List[Union[str, Product]], Union[str, Product]]] = Field(
        None,
        description="The product or service this support contact point is related to (such as product support"
     "for a particular product line). This can be a specific product or product line (e.g. \"iPhone\")"
     "or a general category of products or services (e.g. \"smartphones\").",
    )
    locals().update({"@type": Field("ContactPoint", const=True)})


ContactPoint.update_forward_refs()
