from pydantic import Field
from pydantic_schema_org.EntertainmentBusiness import EntertainmentBusiness


class NightClub(EntertainmentBusiness):
    """A nightclub or discotheque.

    See https://schema.org/NightClub.

    """

    locals().update({"@type": Field("NightClub", const=True)})


NightClub.update_forward_refs()
