from pydantic import Field
from pydantic_schemaorg.SportsActivityLocation import SportsActivityLocation


class TennisComplex(SportsActivityLocation):
    """A tennis complex.

    See https://schema.org/TennisComplex.

    """
    type_: str = Field("TennisComplex", const=True, alias='@type')
    

TennisComplex.update_forward_refs()
