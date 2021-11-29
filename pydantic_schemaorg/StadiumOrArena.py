from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure
from pydantic_schemaorg.SportsActivityLocation import SportsActivityLocation


class StadiumOrArena(CivicStructure, SportsActivityLocation):
    """A stadium.

    See https://schema.org/StadiumOrArena.

    """

    locals().update({"@type": Field("StadiumOrArena", const=True)})


StadiumOrArena.update_forward_refs()
