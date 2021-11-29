from pydantic import Field, AnyUrl, StrictBool
from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
from decimal import Decimal
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Residence import Residence


class ApartmentComplex(Residence):
    """Residence type: Apartment complex.

    See https://schema.org/ApartmentComplex.

    """

    numberOfBedrooms: Optional[Union[List[Union[Decimal, QuantitativeValue]], Union[Decimal, QuantitativeValue]]] = Field(
        None,
        description="The total integer number of bedrooms in a some [[Accommodation]], [[ApartmentComplex]]"
     "or [[FloorPlan]].",
    )
    tourBookingPage: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None,
        description="A page providing information on how to book a tour of some [[Place]], such as an [[Accommodation]]"
     "or [[ApartmentComplex]] in a real estate setting, as well as other kinds of tours as appropriate.",
    )
    numberOfAccommodationUnits: Optional[Union[List[QuantitativeValue], QuantitativeValue]] = Field(
        None,
        description="Indicates the total (available plus unavailable) number of accommodation units in"
     "an [[ApartmentComplex]], or the number of accommodation units for a specific [[FloorPlan]]"
     "(within its specific [[ApartmentComplex]]). See also [[numberOfAvailableAccommodationUnits]].",
    )
    petsAllowed: Optional[Union[List[Union[str, StrictBool]], Union[str, StrictBool]]] = Field(
        None,
        description="Indicates whether pets are allowed to enter the accommodation or lodging business."
     "More detailed information can be put in a text value.",
    )
    numberOfAvailableAccommodationUnits: Optional[Union[List[QuantitativeValue], QuantitativeValue]] = Field(
        None,
        description="Indicates the number of available accommodation units in an [[ApartmentComplex]],"
     "or the number of accommodation units for a specific [[FloorPlan]] (within its specific"
     "[[ApartmentComplex]]). See also [[numberOfAccommodationUnits]].",
    )
    locals().update({"@type": Field("ApartmentComplex", const=True)})


ApartmentComplex.update_forward_refs()
