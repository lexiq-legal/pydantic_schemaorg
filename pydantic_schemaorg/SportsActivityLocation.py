from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class SportsActivityLocation(LocalBusiness):
    """A sports location, such as a playing field.

    See https://schema.org/SportsActivityLocation.

    """
    type_: str = Field("SportsActivityLocation", const=True, alias='@type')
    

SportsActivityLocation.update_forward_refs()
