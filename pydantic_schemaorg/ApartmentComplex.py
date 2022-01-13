from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.Residence import Residence


class ApartmentComplex(Residence):
    """Residence type: Apartment complex.

    See: https://schema.org/ApartmentComplex
    Model depth: 4
    """

    type_: str = Field("ApartmentComplex", const=True, alias="@type")
    numberOfBedrooms: "Optional[Union[List[Union[Decimal, QuantitativeValue, str]], Union[Decimal, QuantitativeValue, str]]]" = Field(
        None,
        description="The total integer number of bedrooms in a some [[Accommodation]], [[ApartmentComplex]]"
        "or [[FloorPlan]].",
    )
    tourBookingPage: "Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]]" = Field(
        None,
        description="A page providing information on how to book a tour of some [[Place]], such as an [[Accommodation]]"
        "or [[ApartmentComplex]] in a real estate setting, as well as other kinds of tours as appropriate.",
    )
    numberOfAccommodationUnits: "Optional[Union[List[Union[QuantitativeValue, str]], Union[QuantitativeValue, str]]]" = Field(
        None,
        description="Indicates the total (available plus unavailable) number of accommodation units in"
        "an [[ApartmentComplex]], or the number of accommodation units for a specific [[FloorPlan]]"
        "(within its specific [[ApartmentComplex]]). See also [[numberOfAvailableAccommodationUnits]].",
    )
    petsAllowed: "Optional[Union[List[Union[str, StrictBool]], Union[str, StrictBool]]]" = Field(
        None,
        description="Indicates whether pets are allowed to enter the accommodation or lodging business."
        "More detailed information can be put in a text value.",
    )
    numberOfAvailableAccommodationUnits: "Optional[Union[List[Union[QuantitativeValue, str]], Union[QuantitativeValue, str]]]" = Field(
        None,
        description="Indicates the number of available accommodation units in an [[ApartmentComplex]],"
        "or the number of accommodation units for a specific [[FloorPlan]] (within its specific"
        "[[ApartmentComplex]]). See also [[numberOfAccommodationUnits]].",
    )


if TYPE_CHECKING:

    from decimal import Decimal

    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue

    from pydantic import AnyUrl, StrictBool

    ApartmentComplex.update_forward_refs()
