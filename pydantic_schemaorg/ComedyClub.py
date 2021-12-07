from pydantic import Field
from pydantic_schemaorg.EntertainmentBusiness import EntertainmentBusiness


class ComedyClub(EntertainmentBusiness):
    """A comedy club.

    See https://schema.org/ComedyClub.

    """
    type_: str = Field("ComedyClub", const=True, alias='@type')
    

ComedyClub.update_forward_refs()
