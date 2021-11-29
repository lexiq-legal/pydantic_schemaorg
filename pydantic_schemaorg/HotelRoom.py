from pydantic import Field
from pydantic_schemaorg.BedDetails import BedDetails
from typing import Any, Union, List, Optional
from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
from pydantic_schemaorg.Room import Room


class HotelRoom(Room):
    """A hotel room is a single room in a hotel. <br /><br /> See also the <a href=\"/docs/hotels.html\">dedicated"
     "document on the use of schema.org for marking up hotels and other forms of accommodations</a>.

    See https://schema.org/HotelRoom.

    """

    bed: Union[List[Union[str, BedDetails, Any]], Union[str, BedDetails, Any]] = Field(
        None,
        description="The type of bed or beds included in the accommodation. For the single case of just one bed"
     "of a certain type, you use bed directly with a text. If you want to indicate the quantity"
     "of a certain kind of bed, use an instance of BedDetails. For more detailed information,"
     "use the amenityFeature property.",
    )
    occupancy: Optional[Union[List[QuantitativeValue], QuantitativeValue]] = Field(
        None,
        description="The allowed total occupancy for the accommodation in persons (including infants etc)."
     "For individual accommodations, this is not necessarily the legal maximum but defines"
     "the permitted usage as per the contractual agreement (e.g. a double room used by a single"
     "person). Typical unit code(s): C62 for person",
    )
    locals().update({"@type": Field("HotelRoom", const=True)})


HotelRoom.update_forward_refs()
