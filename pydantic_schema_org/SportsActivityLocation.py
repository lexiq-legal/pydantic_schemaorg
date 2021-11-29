from pydantic import Field
from pydantic_schema_org.LocalBusiness import LocalBusiness


class SportsActivityLocation(LocalBusiness):
    """A sports location, such as a playing field.

    See https://schema.org/SportsActivityLocation.

    """

    locals().update({"@type": Field("SportsActivityLocation", const=True)})


SportsActivityLocation.update_forward_refs()
