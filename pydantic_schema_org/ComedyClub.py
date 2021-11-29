from pydantic import Field
from pydantic_schema_org.EntertainmentBusiness import EntertainmentBusiness


class ComedyClub(EntertainmentBusiness):
    """A comedy club.

    See https://schema.org/ComedyClub.

    """

    locals().update({"@type": Field("ComedyClub", const=True)})


ComedyClub.update_forward_refs()
