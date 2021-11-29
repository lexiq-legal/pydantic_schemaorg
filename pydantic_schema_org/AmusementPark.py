from pydantic import Field
from pydantic_schema_org.EntertainmentBusiness import EntertainmentBusiness


class AmusementPark(EntertainmentBusiness):
    """An amusement park.

    See https://schema.org/AmusementPark.

    """

    locals().update({"@type": Field("AmusementPark", const=True)})


AmusementPark.update_forward_refs()
