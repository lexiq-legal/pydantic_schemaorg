from pydantic import Field
from pydantic_schemaorg.EntertainmentBusiness import EntertainmentBusiness


class AmusementPark(EntertainmentBusiness):
    """An amusement park.

    See https://schema.org/AmusementPark.

    """
    type_: str = Field("AmusementPark", const=True, alias='@type')
    

AmusementPark.update_forward_refs()
