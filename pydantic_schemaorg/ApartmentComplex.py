from __future__ import annotations
from typing import TYPE_CHECKING

from decimal import Decimal
from typing import Union, Optional, List
from pydantic import StrictBool, AnyUrl


from pydantic import Field
from pydantic_schemaorg.Residence import Residence


class ApartmentComplex(Residence):
    """Residence type: Apartment complex.

    See: https://schema.org/ApartmentComplex
    Model depth: 4
    """
    type_: str = Field("ApartmentComplex", alias='@type')
    numberOfBedrooms: Optional[Union[List[Union[Decimal, 'Number', 'QuantitativeValue', str]], Decimal, 'Number', 'QuantitativeValue', str]] = Field(
        None,
        description="The total integer number of bedrooms in a some [[Accommodation]], [[ApartmentComplex]]"
     "or [[FloorPlan]].",
    )
    tourBookingPage: Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]] = Field(
        None,
        description="A page providing information on how to book a tour of some [[Place]], such as an [[Accommodation]]"
     "or [[ApartmentComplex]] in a real estate setting, as well as other kinds of tours as appropriate.",
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
    numberOfAvailableAccommodationUnits: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        None,
        description="Indicates the number of available accommodation units in an [[ApartmentComplex]],"
     "or the number of accommodation units for a specific [[FloorPlan]] (within its specific"
     "[[ApartmentComplex]]). See also [[numberOfAccommodationUnits]].",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.Text import Text
