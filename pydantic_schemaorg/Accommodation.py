from pydantic import Field, AnyUrl, StrictBool
from decimal import Decimal
from typing import Any, Union, List, Optional
from pydantic_schemaorg.LocationFeatureSpecification import LocationFeatureSpecification
from pydantic_schemaorg.Place import Place


class Accommodation(Place):
    """An accommodation is a place that can accommodate human beings, e.g. a hotel room, a camping"
     "pitch, or a meeting room. Many accommodations are for overnight stays, but this is not"
     "a mandatory requirement. For more specific types of accommodations not defined in schema.org,"
     "one can use additionalType with external vocabularies. <br /><br /> See also the <a href=\"/docs/hotels.html\">dedicated"
     "document on the use of schema.org for marking up hotels and other forms of accommodations</a>.

    See https://schema.org/Accommodation.

    """

    numberOfBedrooms: Union[List[Union[Decimal, Any]], Union[Decimal, Any]] = Field(
        None,
        description="The total integer number of bedrooms in a some [[Accommodation]], [[ApartmentComplex]]"
     "or [[FloorPlan]].",
    )
    numberOfBathroomsTotal: Optional[Union[List[int], int]] = Field(
        None,
        description="The total integer number of bathrooms in a some [[Accommodation]], following real estate"
     "conventions as [documented in RESO](https://ddwiki.reso.org/display/DDW17/BathroomsTotalInteger+Field):"
     "\"The simple sum of the number of bathrooms. For example for a property with two Full Bathrooms"
     "and one Half Bathroom, the Bathrooms Total Integer will be 3.\". See also [[numberOfRooms]].",
    )
    permittedUsage: Optional[Union[List[str], str]] = Field(
        None,
        description="Indications regarding the permitted usage of the accommodation.",
    )
    numberOfPartialBathrooms: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="Number of partial bathrooms - The total number of half and ¼ bathrooms in an [[Accommodation]]."
     "This corresponds to the [BathroomsPartial field in RESO](https://ddwiki.reso.org/display/DDW17/BathroomsPartial+Field).",
    )
    yearBuilt: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="The year an [[Accommodation]] was constructed. This corresponds to the [YearBuilt"
     "field in RESO](https://ddwiki.reso.org/display/DDW17/YearBuilt+Field).",
    )
    leaseLength: Any = Field(
        None,
        description="Length of the lease for some [[Accommodation]], either particular to some [[Offer]]"
     "or in some cases intrinsic to the property.",
    )
    amenityFeature: Optional[Union[List[LocationFeatureSpecification], LocationFeatureSpecification]] = Field(
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
    tourBookingPage: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None,
        description="A page providing information on how to book a tour of some [[Place]], such as an [[Accommodation]]"
     "or [[ApartmentComplex]] in a real estate setting, as well as other kinds of tours as appropriate.",
    )
    petsAllowed: Optional[Union[List[Union[str, StrictBool]], Union[str, StrictBool]]] = Field(
        None,
        description="Indicates whether pets are allowed to enter the accommodation or lodging business."
     "More detailed information can be put in a text value.",
    )
    accommodationCategory: Optional[Union[List[str], str]] = Field(
        None,
        description="Category of an [[Accommodation]], following real estate conventions e.g. RESO (see"
     "[PropertySubType](https://ddwiki.reso.org/display/DDW17/PropertySubType+Field),"
     "and [PropertyType](https://ddwiki.reso.org/display/DDW17/PropertyType+Field)"
     "fields for suggested values).",
    )
    floorLevel: Optional[Union[List[str], str]] = Field(
        None,
        description="The floor level for an [[Accommodation]] in a multi-storey building. Since counting"
     "systems [vary internationally](https://en.wikipedia.org/wiki/Storey#Consecutive_number_floor_designations),"
     "the local system should be used where possible.",
    )
    floorSize: Any = Field(
        None,
        description="The size of the accommodation, e.g. in square meter or squarefoot. Typical unit code(s):"
     "MTK for square meter, FTK for square foot, or YDK for square yard",
    )
    accommodationFloorPlan: Any = Field(
        None,
        description="A floorplan of some [[Accommodation]].",
    )
    numberOfFullBathrooms: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="Number of full bathrooms - The total number of full and ¾ bathrooms in an [[Accommodation]]."
     "This corresponds to the [BathroomsFull field in RESO](https://ddwiki.reso.org/display/DDW17/BathroomsFull+Field).",
    )
    locals().update({"@type": Field("Accommodation", const=True)})


Accommodation.update_forward_refs()
