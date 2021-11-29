from pydantic import Field, AnyUrl
from pydantic_schemaorg.Duration import Duration
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Place import Place
from pydantic_schemaorg.PostalAddress import PostalAddress
from pydantic_schemaorg.Service import Service
from pydantic_schemaorg.ContactPoint import ContactPoint
from pydantic_schemaorg.Intangible import Intangible


class ServiceChannel(Intangible):
    """A means for accessing a service, e.g. a government office location, web site, or phone"
     "number.

    See https://schema.org/ServiceChannel.

    """

    processingTime: Optional[Union[List[Duration], Duration]] = Field(
        None,
        description="Estimated processing time for the service using this channel.",
    )
    serviceLocation: Optional[Union[List[Place], Place]] = Field(
        None,
        description="The location (e.g. civic structure, local business, etc.) where a person can go to access"
     "the service.",
    )
    servicePostalAddress: Optional[Union[List[PostalAddress], PostalAddress]] = Field(
        None,
        description="The address for accessing the service by mail.",
    )
    serviceUrl: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None,
        description="The website to access the service.",
    )
    providesService: Optional[Union[List[Service], Service]] = Field(
        None,
        description="The service provided by this channel.",
    )
    serviceSmsNumber: Optional[Union[List[ContactPoint], ContactPoint]] = Field(
        None,
        description="The number to access the service by text message.",
    )
    servicePhone: Optional[Union[List[ContactPoint], ContactPoint]] = Field(
        None,
        description="The phone number to use to access the service.",
    )
    availableLanguage: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="A language someone may use with or at the item, service or place. Please use one of the language"
     "codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also"
     "[[inLanguage]]",
    )
    locals().update({"@type": Field("ServiceChannel", const=True)})


ServiceChannel.update_forward_refs()
