from pydantic import Field
from decimal import Decimal
from typing import List, Optional, Union
from pydantic_schemaorg.BedType import BedType
from pydantic_schemaorg.Intangible import Intangible


class BedDetails(Intangible):
    """An entity holding detailed information about the available bed types, e.g. the quantity"
     "of twin beds for a hotel room. For the single case of just one bed of a certain type, you can"
     "use bed directly with a text. See also [[BedType]] (under development).

    See https://schema.org/BedDetails.

    """
    type_: str = Field("BedDetails", const=True, alias='@type')
    numberOfBeds: Optional[Union[List[Union[Decimal, str]], Union[Decimal, str]]] = Field(
        None,
        description="The quantity of the given bed type available in the HotelRoom, Suite, House, or Apartment.",
    )
    typeOfBed: Optional[Union[List[Union[str, BedType]], Union[str, BedType]]] = Field(
        None,
        description="The type of bed to which the BedDetail refers, i.e. the type of bed available in the quantity"
     "indicated by quantity.",
    )
    

BedDetails.update_forward_refs()
