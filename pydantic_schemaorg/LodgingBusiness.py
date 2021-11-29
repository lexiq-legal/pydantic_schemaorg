from pydantic import Field, StrictBool
from typing import Any, Union, List, Optional
from decimal import Decimal
from datetime import datetime, time
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class LodgingBusiness(LocalBusiness):
    """A lodging business, such as a motel, hotel, or inn.

    See https://schema.org/LodgingBusiness.

    """

    amenityFeature: Any = Field(
        None,
        description="An amenity feature (e.g. a characteristic or service) of the Accommodation. This generic"
     "property does not make a statement about whether the feature is included in an offer for"
     "the main accommodation or available at extra costs.",
    )
    numberOfRooms: Union[List[Union[Decimal, Any]], Union[Decimal, Any]] = Field(
        None,
        description="The number of rooms (excluding bathrooms and closets) of the accommodation or lodging"
     "business. Typical unit code(s): ROM for room or C62 for no unit. The type of room can be"
     "put in the unitText property of the QuantitativeValue.",
    )
    starRating: Any = Field(
        None,
        description="An official rating for a lodging business or food establishment, e.g. from national"
     "associations or standards bodies. Use the author property to indicate the rating organization,"
     "e.g. as an Organization with name such as (e.g. HOTREC, DEHOGA, WHR, or Hotelstars).",
    )
    checkinTime: Optional[Union[List[Union[datetime, time]], Union[datetime, time]]] = Field(
        None,
        description="The earliest someone may check into a lodging establishment.",
    )
    petsAllowed: Optional[Union[List[Union[str, StrictBool]], Union[str, StrictBool]]] = Field(
        None,
        description="Indicates whether pets are allowed to enter the accommodation or lodging business."
     "More detailed information can be put in a text value.",
    )
    audience: Any = Field(
        None,
        description="An intended audience, i.e. a group for whom something was created.",
    )
    availableLanguage: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="A language someone may use with or at the item, service or place. Please use one of the language"
     "codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also"
     "[[inLanguage]]",
    )
    checkoutTime: Optional[Union[List[Union[datetime, time]], Union[datetime, time]]] = Field(
        None,
        description="The latest someone may check out of a lodging establishment.",
    )
    locals().update({"@type": Field("LodgingBusiness", const=True)})


LodgingBusiness.update_forward_refs()
