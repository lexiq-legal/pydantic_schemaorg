from pydantic import Field
from pydantic_schemaorg.SportsActivityLocation import SportsActivityLocation


class SportsClub(SportsActivityLocation):
    """A sports club.

    See https://schema.org/SportsClub.

    """

    locals().update({"@type": Field("SportsClub", const=True)})


SportsClub.update_forward_refs()
