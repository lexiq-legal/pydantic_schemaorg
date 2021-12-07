from pydantic import Field
from pydantic_schemaorg.SportsActivityLocation import SportsActivityLocation


class BowlingAlley(SportsActivityLocation):
    """A bowling alley.

    See https://schema.org/BowlingAlley.

    """
    type_: str = Field("BowlingAlley", const=True, alias='@type')
    

BowlingAlley.update_forward_refs()
