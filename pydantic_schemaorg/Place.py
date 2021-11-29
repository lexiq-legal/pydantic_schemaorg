from pydantic import Field, AnyUrl, StrictBool
from typing import Any, Union, List, Optional
from decimal import Decimal
from pydantic_schemaorg.Thing import Thing


class Place(Thing):
    """Entities that have a somewhat fixed, physical extension.

    See https://schema.org/Place.

    """

    geo: Any = Field(
        None,
        description="The geo coordinates of the place.",
    )
    geoEquals: Any = Field(
        None,
        description="Represents spatial relations in which two geometries (or the places they represent)"
     "are topologically equal, as defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM)."
     "\"Two geometries are topologically equal if their interiors intersect and no part of"
     "the interior or boundary of one geometry intersects the exterior of the other\" (a symmetric"
     "relationship)",
    )
    publicAccess: Optional[Union[List[StrictBool], StrictBool]] = Field(
        None,
        description="A flag to signal that the [[Place]] is open to public visitors. If this property is omitted"
     "there is no assumed default boolean value",
    )
    geoDisjoint: Any = Field(
        None,
        description="Represents spatial relations in which two geometries (or the places they represent)"
     "are topologically disjoint: they have no point in common. They form a set of disconnected"
     "geometries.\" (a symmetric relationship, as defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM))",
    )
    geoTouches: Any = Field(
        None,
        description="Represents spatial relations in which two geometries (or the places they represent)"
     "touch: they have at least one boundary point in common, but no interior points.\" (a symmetric"
     "relationship, as defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM) )",
    )
    specialOpeningHoursSpecification: Any = Field(
        None,
        description="The special opening hours of a certain place. Use this to explicitly override general"
     "opening hours brought in scope by [[openingHoursSpecification]] or [[openingHours]].",
    )
    globalLocationNumber: Optional[Union[List[str], str]] = Field(
        None,
        description="The [Global Location Number](http://www.gs1.org/gln) (GLN, sometimes also referred"
     "to as International Location Number or ILN) of the respective organization, person,"
     "or place. The GLN is a 13-digit number used to identify parties and physical locations.",
    )
    hasDriveThroughService: Optional[Union[List[StrictBool], StrictBool]] = Field(
        None,
        description="Indicates whether some facility (e.g. [[FoodEstablishment]], [[CovidTestingFacility]])"
     "offers a service that can be used by driving through in a car. In the case of [[CovidTestingFacility]]"
     "such facilities could potentially help with social distancing from other potentially-infected"
     "users.",
    )
    maximumAttendeeCapacity: Optional[Union[List[int], int]] = Field(
        None,
        description="The total number of individuals that may attend an event or venue.",
    )
    photo: Any = Field(
        None,
        description="A photograph of this place.",
    )
    aggregateRating: Any = Field(
        None,
        description="The overall rating, based on a collection of reviews or ratings, of the item.",
    )
    containedIn: Any = Field(
        None,
        description="The basic containment relation between a place and one that contains it.",
    )
    isicV4: Optional[Union[List[str], str]] = Field(
        None,
        description="The International Standard of Industrial Classification of All Economic Activities"
     "(ISIC), Revision 4 code for a particular organization, business person, or place.",
    )
    longitude: Optional[Union[List[Union[Decimal, str]], Union[Decimal, str]]] = Field(
        None,
        description="The longitude of a location. For example ```-122.08585``` ([WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System)).",
    )
    smokingAllowed: Optional[Union[List[StrictBool], StrictBool]] = Field(
        None,
        description="Indicates whether it is allowed to smoke in the place, e.g. in the restaurant, hotel or"
     "hotel room.",
    )
    amenityFeature: Any = Field(
        None,
        description="An amenity feature (e.g. a characteristic or service) of the Accommodation. This generic"
     "property does not make a statement about whether the feature is included in an offer for"
     "the main accommodation or available at extra costs.",
    )
    geoCovers: Any = Field(
        None,
        description="Represents a relationship between two geometries (or the places they represent), relating"
     "a covering geometry to a covered geometry. \"Every point of b is a point of (the interior"
     "or boundary of) a\". As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).",
    )
    containsPlace: Any = Field(
        None,
        description="The basic containment relation between a place and another that it contains.",
    )
    slogan: Optional[Union[List[str], str]] = Field(
        None,
        description="A slogan or motto associated with the item.",
    )
    containedInPlace: Any = Field(
        None,
        description="The basic containment relation between a place and one that contains it.",
    )
    branchCode: Optional[Union[List[str], str]] = Field(
        None,
        description="A short textual code (also called \"store code\") that uniquely identifies a place of"
     "business. The code is typically assigned by the parentOrganization and used in structured"
     "URLs. For example, in the URL http://www.starbucks.co.uk/store-locator/etc/detail/3047"
     "the code \"3047\" is a branchCode for a particular branch.",
    )
    geoContains: Any = Field(
        None,
        description="Represents a relationship between two geometries (or the places they represent), relating"
     "a containing geometry to a contained geometry. \"a contains b iff no points of b lie in"
     "the exterior of a, and at least one point of the interior of b lies in the interior of a\"."
     "As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).",
    )
    tourBookingPage: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None,
        description="A page providing information on how to book a tour of some [[Place]], such as an [[Accommodation]]"
     "or [[ApartmentComplex]] in a real estate setting, as well as other kinds of tours as appropriate.",
    )
    geoCoveredBy: Any = Field(
        None,
        description="Represents a relationship between two geometries (or the places they represent), relating"
     "a geometry to another that covers it. As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).",
    )
    photos: Any = Field(
        None,
        description="Photographs of this place.",
    )
    geoCrosses: Any = Field(
        None,
        description="Represents a relationship between two geometries (or the places they represent), relating"
     "a geometry to another that crosses it: \"a crosses b: they have some but not all interior"
     "points in common, and the dimension of the intersection is less than that of at least one"
     "of them\". As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).",
    )
    geoWithin: Any = Field(
        None,
        description="Represents a relationship between two geometries (or the places they represent), relating"
     "a geometry to one that contains it, i.e. it is inside (i.e. within) its interior. As defined"
     "in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).",
    )
    geoIntersects: Any = Field(
        None,
        description="Represents spatial relations in which two geometries (or the places they represent)"
     "have at least one point in common. As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).",
    )
    logo: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="An associated logo.",
    )
    latitude: Optional[Union[List[Union[Decimal, str]], Union[Decimal, str]]] = Field(
        None,
        description="The latitude of a location. For example ```37.42242``` ([WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System)).",
    )
    address: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="Physical address of the item.",
    )
    maps: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None,
        description="A URL to a map of the place.",
    )
    events: Any = Field(
        None,
        description="Upcoming or past events associated with this place or organization.",
    )
    geoOverlaps: Any = Field(
        None,
        description="Represents a relationship between two geometries (or the places they represent), relating"
     "a geometry to another that geospatially overlaps it, i.e. they have some but not all points"
     "in common. As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).",
    )
    reviews: Any = Field(
        None,
        description="Review of the item.",
    )
    telephone: Optional[Union[List[str], str]] = Field(
        None,
        description="The telephone number.",
    )
    openingHoursSpecification: Any = Field(
        None,
        description="The opening hours of a certain place.",
    )
    review: Any = Field(
        None,
        description="A review of the item.",
    )
    map: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None,
        description="A URL to a map of the place.",
    )
    additionalProperty: Any = Field(
        None,
        description="A property-value pair representing an additional characteristics of the entitity,"
     "e.g. a product feature or another characteristic for which there is no matching property"
     "in schema.org. Note: Publishers should be aware that applications designed to use specific"
     "schema.org properties (e.g. https://schema.org/width, https://schema.org/color,"
     "https://schema.org/gtin13, ...) will typically expect such data to be provided using"
     "those properties, rather than using the generic property/value mechanism.",
    )
    isAccessibleForFree: Optional[Union[List[StrictBool], StrictBool]] = Field(
        None,
        description="A flag to signal that the item, event, or place is accessible for free.",
    )
    event: Any = Field(
        None,
        description="Upcoming or past event associated with this place, organization, or action.",
    )
    hasMap: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="A URL to a map of the place.",
    )
    faxNumber: Optional[Union[List[str], str]] = Field(
        None,
        description="The fax number.",
    )
    locals().update({"@type": Field("Place", const=True)})


Place.update_forward_refs()
