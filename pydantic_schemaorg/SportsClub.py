from pydantic import Field
from pydantic_schemaorg.SportsActivityLocation import SportsActivityLocation


class SportsClub(SportsActivityLocation):
    """A sports club.

    See https://schema.org/SportsClub.

    """
    type_: str = Field("SportsClub", const=True, alias='@type')
    

SportsClub.update_forward_refs()
