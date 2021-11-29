from pydantic import Field
from pydantic_schema_org.SportsActivityLocation import SportsActivityLocation
from pydantic_schema_org.CivicStructure import CivicStructure


class StadiumOrArena(SportsActivityLocation, CivicStructure):
    """A stadium.

    See https://schema.org/StadiumOrArena.

    """

    locals().update({"@type": Field("StadiumOrArena", const=True)})


StadiumOrArena.update_forward_refs()
