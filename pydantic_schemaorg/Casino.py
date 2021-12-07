from pydantic import Field
from pydantic_schemaorg.EntertainmentBusiness import EntertainmentBusiness


class Casino(EntertainmentBusiness):
    """A casino.

    See https://schema.org/Casino.

    """
    type_: str = Field("Casino", const=True, alias='@type')
    

Casino.update_forward_refs()
