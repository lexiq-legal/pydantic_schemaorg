from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.Intangible import Intangible


class ServiceChannel(Intangible):
    """A means for accessing a service, e.g. a government office location, web site, or phone"
     "number.

    See: https://schema.org/ServiceChannel
    Model depth: 3
    """

    type_: str = Field("ServiceChannel", const=True, alias="@type")
    processingTime: "Optional[Union[List[Union[Duration, str]], Union[Duration, str]]]" = Field(
        None,
        description="Estimated processing time for the service using this channel.",
    )
    serviceLocation: "Optional[Union[List[Union[Place, str]], Union[Place, str]]]" = Field(
        None,
        description="The location (e.g. civic structure, local business, etc.) where a person can go to access"
        "the service.",
    )
    servicePostalAddress: "Optional[Union[List[Union[PostalAddress, str]], Union[PostalAddress, str]]]" = Field(
        None,
        description="The address for accessing the service by mail.",
    )
    serviceUrl: "Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]]" = Field(
        None,
        description="The website to access the service.",
    )
    providesService: "Optional[Union[List[Union[Service, str]], Union[Service, str]]]" = Field(
        None,
        description="The service provided by this channel.",
    )
    serviceSmsNumber: "Optional[Union[List[Union[ContactPoint, str]], Union[ContactPoint, str]]]" = Field(
        None,
        description="The number to access the service by text message.",
    )
    servicePhone: "Optional[Union[List[Union[ContactPoint, str]], Union[ContactPoint, str]]]" = Field(
        None,
        description="The phone number to use to access the service.",
    )
    availableLanguage: "Optional[Union[List[Union[str, Language]], Union[str, Language]]]" = Field(
        None,
        description="A language someone may use with or at the item, service or place. Please use one of the language"
        "codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also"
        "[[inLanguage]]",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.Duration import Duration

    from pydantic_schemaorg.Place import Place

    from pydantic_schemaorg.PostalAddress import PostalAddress

    from pydantic import AnyUrl

    from pydantic_schemaorg.Service import Service

    from pydantic_schemaorg.ContactPoint import ContactPoint

    from pydantic_schemaorg.Language import Language

    ServiceChannel.update_forward_refs()
