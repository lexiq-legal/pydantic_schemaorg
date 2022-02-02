from __future__ import annotations
from typing import TYPE_CHECKING

from decimal import Decimal
from typing import Union, Optional, List
from pydantic import StrictBool, AnyUrl


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class FloorPlan(Intangible):
    """A FloorPlan is an explicit representation of a collection of similar accommodations,"
     "allowing the provision of common information (room counts, sizes, layout diagrams)"
     "and offers for rental or sale. In typical use, some [[ApartmentComplex]] has an [[accommodationFloorPlan]]"
     "which is a [[FloorPlan]]. A FloorPlan is always in the context of a particular place,"
     "either a larger [[ApartmentComplex]] or a single [[Apartment]]. The visual/spatial"
     "aspects of a floor plan (i.e. room layout, [see wikipedia](https://en.wikipedia.org/wiki/Floor_plan))"
     "can be indicated using [[image]].

    See: https://schema.org/FloorPlan
    Model depth: 3
    """
    type_: str = Field("FloorPlan", alias='@type')
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
    numberOfPartialBathrooms: Optional[Union[List[Union[Decimal, 'Number', str]], Decimal, 'Number', str]] = Field(
        None,
        description="Number of partial bathrooms - The total number of half and ¼ bathrooms in an [[Accommodation]]."
     "This corresponds to the [BathroomsPartial field in RESO](https://ddwiki.reso.org/display/DDW17/BathroomsPartial+Field).",
    )
    layoutImage: Optional[Union[List[Union[AnyUrl, 'URL', 'ImageObject', str]], AnyUrl, 'URL', 'ImageObject', str]] = Field(
        None,
        description="A schematic image showing the floorplan layout.",
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
    numberOfAccommodationUnits: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        None,
        description="Indicates the total (available plus unavailable) number of accommodation units in"
     "an [[ApartmentComplex]], or the number of accommodation units for a specific [[FloorPlan]]"
     "(within its specific [[ApartmentComplex]]). See also [[numberOfAvailableAccommodationUnits]].",
    )
    petsAllowed: Optional[Union[List[Union[StrictBool, 'Boolean', str, 'Text']], StrictBool, 'Boolean', str, 'Text']] = Field(
        None,
        description="Indicates whether pets are allowed to enter the accommodation or lodging business."
     "More detailed information can be put in a text value.",
    )
    floorSize: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        None,
        description="The size of the accommodation, e.g. in square meter or squarefoot. Typical unit code(s):"
     "MTK for square meter, FTK for square foot, or YDK for square yard",
    )
    isPlanForApartment: Optional[Union[List[Union['Accommodation', str]], 'Accommodation', str]] = Field(
        None,
        description="Indicates some accommodation that this floor plan describes.",
    )
    numberOfFullBathrooms: Optional[Union[List[Union[Decimal, 'Number', str]], Decimal, 'Number', str]] = Field(
        None,
        description="Number of full bathrooms - The total number of full and ¾ bathrooms in an [[Accommodation]]."
     "This corresponds to the [BathroomsFull field in RESO](https://ddwiki.reso.org/display/DDW17/BathroomsFull+Field).",
    )
    numberOfAvailableAccommodationUnits: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        None,
        description="Indicates the number of available accommodation units in an [[ApartmentComplex]],"
     "or the number of accommodation units for a specific [[FloorPlan]] (within its specific"
     "[[ApartmentComplex]]). See also [[numberOfAccommodationUnits]].",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.LocationFeatureSpecification import LocationFeatureSpecification
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Accommodation import Accommodation
