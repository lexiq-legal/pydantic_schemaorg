from __future__ import annotations
from typing import TYPE_CHECKING

from decimal import Decimal
from typing import Union, Optional, List
from pydantic import StrictBool, AnyUrl


from pydantic import Field
from pydantic_schemaorg.Place import Place


class Accommodation(Place):
    """An accommodation is a place that can accommodate human beings, e.g. a hotel room, a camping"
     "pitch, or a meeting room. Many accommodations are for overnight stays, but this is not"
     "a mandatory requirement. For more specific types of accommodations not defined in schema.org,"
     "one can use additionalType with external vocabularies. <br /><br /> See also the <a href=\"/docs/hotels.html\">dedicated"
     "document on the use of schema.org for marking up hotels and other forms of accommodations</a>.

    See: https://schema.org/Accommodation
    Model depth: 3
    """
    type_: str = Field("Accommodation", alias='@type')
    numberOfBedrooms: Optional[Union[List[Union[Decimal, 'Number', 'QuantitativeValue', str]], Decimal, 'Number', 'QuantitativeValue', str]] = Field(
        None,
        description="The total integer number of bedrooms in a some [[Accommodation]], [[ApartmentComplex]]"
     "or [[FloorPlan]].",
    )
    numberOfBathroomsTotal: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        None,
        description="The total integer number of bathrooms in a some [[Accommodation]], following real estate"
     "conventions as [documented in RESO](https://ddwiki.reso.org/display/DDW17/BathroomsTotalInteger+Field):"
     "\"The simple sum of the number of bathrooms. For example for a property with two Full Bathrooms"
     "and one Half Bathroom, the Bathrooms Total Integer will be 3.\". See also [[numberOfRooms]].",
    )
    permittedUsage: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Indications regarding the permitted usage of the accommodation.",
    )
    numberOfPartialBathrooms: Optional[Union[List[Union[Decimal, 'Number', str]], Decimal, 'Number', str]] = Field(
        None,
        description="Number of partial bathrooms - The total number of half and ¼ bathrooms in an [[Accommodation]]."
     "This corresponds to the [BathroomsPartial field in RESO](https://ddwiki.reso.org/display/DDW17/BathroomsPartial+Field).",
    )
    yearBuilt: Optional[Union[List[Union[Decimal, 'Number', str]], Decimal, 'Number', str]] = Field(
        None,
        description="The year an [[Accommodation]] was constructed. This corresponds to the [YearBuilt"
     "field in RESO](https://ddwiki.reso.org/display/DDW17/YearBuilt+Field).",
    )
    leaseLength: Optional[Union[List[Union['Duration', 'QuantitativeValue', str]], 'Duration', 'QuantitativeValue', str]] = Field(
        None,
        description="Length of the lease for some [[Accommodation]], either particular to some [[Offer]]"
     "or in some cases intrinsic to the property.",
    )
    amenityFeature: Optional[Union[List[Union['LocationFeatureSpecification', str]], 'LocationFeatureSpecification', str]] = Field(
        None,
        description="An amenity feature (e.g. a characteristic or service) of the Accommodation. This generic"
     "property does not make a statement about whether the feature is included in an offer for"
     "the main accommodation or available at extra costs.",
    )
    numberOfRooms: Optional[Union[List[Union[Decimal, 'Number', 'QuantitativeValue', str]], Decimal, 'Number', 'QuantitativeValue', str]] = Field(
        None,
        description="The number of rooms (excluding bathrooms and closets) of the accommodation or lodging"
     "business. Typical unit code(s): ROM for room or C62 for no unit. The type of room can be"
     "put in the unitText property of the QuantitativeValue.",
    )
    tourBookingPage: Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]] = Field(
        None,
        description="A page providing information on how to book a tour of some [[Place]], such as an [[Accommodation]]"
     "or [[ApartmentComplex]] in a real estate setting, as well as other kinds of tours as appropriate.",
    )
    petsAllowed: Optional[Union[List[Union[StrictBool, 'Boolean', str, 'Text']], StrictBool, 'Boolean', str, 'Text']] = Field(
        None,
        description="Indicates whether pets are allowed to enter the accommodation or lodging business."
     "More detailed information can be put in a text value.",
    )
    accommodationCategory: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Category of an [[Accommodation]], following real estate conventions e.g. RESO (see"
     "[PropertySubType](https://ddwiki.reso.org/display/DDW17/PropertySubType+Field),"
     "and [PropertyType](https://ddwiki.reso.org/display/DDW17/PropertyType+Field)"
     "fields for suggested values).",
    )
    floorLevel: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The floor level for an [[Accommodation]] in a multi-storey building. Since counting"
     "systems [vary internationally](https://en.wikipedia.org/wiki/Storey#Consecutive_number_floor_designations),"
     "the local system should be used where possible.",
    )
    floorSize: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        None,
        description="The size of the accommodation, e.g. in square meter or squarefoot. Typical unit code(s):"
     "MTK for square meter, FTK for square foot, or YDK for square yard",
    )
    accommodationFloorPlan: Optional[Union[List[Union['FloorPlan', str]], 'FloorPlan', str]] = Field(
        None,
        description="A floorplan of some [[Accommodation]].",
    )
    numberOfFullBathrooms: Optional[Union[List[Union[Decimal, 'Number', str]], Decimal, 'Number', str]] = Field(
        None,
        description="Number of full bathrooms - The total number of full and ¾ bathrooms in an [[Accommodation]]."
     "This corresponds to the [BathroomsFull field in RESO](https://ddwiki.reso.org/display/DDW17/BathroomsFull+Field).",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Duration import Duration
    from pydantic_schemaorg.LocationFeatureSpecification import LocationFeatureSpecification
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.FloorPlan import FloorPlan
