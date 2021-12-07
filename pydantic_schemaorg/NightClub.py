from pydantic import Field
from pydantic_schemaorg.EntertainmentBusiness import EntertainmentBusiness


class NightClub(EntertainmentBusiness):
    """A nightclub or discotheque.

    See https://schema.org/NightClub.

    """
    type_: str = Field("NightClub", const=True, alias='@type')
    

NightClub.update_forward_refs()
