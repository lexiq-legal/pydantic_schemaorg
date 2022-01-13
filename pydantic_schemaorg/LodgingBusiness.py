from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.LocalBusiness import LocalBusiness


class LodgingBusiness(LocalBusiness):
    """A lodging business, such as a motel, hotel, or inn.

    See: https://schema.org/LodgingBusiness
    Model depth: 4
    """

    type_: str = Field("LodgingBusiness", const=True, alias="@type")
    amenityFeature: "Optional[Union[List[Union[LocationFeatureSpecification, str]], Union[LocationFeatureSpecification, str]]]" = Field(
        None,
        description="An amenity feature (e.g. a characteristic or service) of the Accommodation. This generic"
        "property does not make a statement about whether the feature is included in an offer for"
        "the main accommodation or available at extra costs.",
    )
    numberOfRooms: "Optional[Union[List[Union[Decimal, QuantitativeValue, str]], Union[Decimal, QuantitativeValue, str]]]" = Field(
        None,
        description="The number of rooms (excluding bathrooms and closets) of the accommodation or lodging"
        "business. Typical unit code(s): ROM for room or C62 for no unit. The type of room can be"
        "put in the unitText property of the QuantitativeValue.",
    )
    starRating: "Optional[Union[List[Union[Rating, str]], Union[Rating, str]]]" = Field(
        None,
        description="An official rating for a lodging business or food establishment, e.g. from national"
        "associations or standards bodies. Use the author property to indicate the rating organization,"
        "e.g. as an Organization with name such as (e.g. HOTREC, DEHOGA, WHR, or Hotelstars).",
    )
    checkinTime: "Optional[Union[List[Union[datetime, time, str]], Union[datetime, time, str]]]" = Field(
        None,
        description="The earliest someone may check into a lodging establishment.",
    )
    petsAllowed: "Optional[Union[List[Union[str, StrictBool]], Union[str, StrictBool]]]" = Field(
        None,
        description="Indicates whether pets are allowed to enter the accommodation or lodging business."
        "More detailed information can be put in a text value.",
    )
    audience: "Optional[Union[List[Union[Audience, str]], Union[Audience, str]]]" = Field(
        None,
        description="An intended audience, i.e. a group for whom something was created.",
    )
    availableLanguage: "Optional[Union[List[Union[str, Language]], Union[str, Language]]]" = Field(
        None,
        description="A language someone may use with or at the item, service or place. Please use one of the language"
        "codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also"
        "[[inLanguage]]",
    )
    checkoutTime: "Optional[Union[List[Union[datetime, time, str]], Union[datetime, time, str]]]" = Field(
        None,
        description="The latest someone may check out of a lodging establishment.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.LocationFeatureSpecification import (
        LocationFeatureSpecification,
    )

    from decimal import Decimal

    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue

    from pydantic_schemaorg.Rating import Rating

    from datetime import time, datetime

    from pydantic import StrictBool

    from pydantic_schemaorg.Audience import Audience

    from pydantic_schemaorg.Language import Language

    LodgingBusiness.update_forward_refs()
