from pydantic import Field
from pydantic_schema_org.SportsActivityLocation import SportsActivityLocation
from pydantic_schema_org.Resort import Resort


class SkiResort(SportsActivityLocation, Resort):
    """A ski resort.

    See https://schema.org/SkiResort.

    """

    locals().update({"@type": Field("SkiResort", const=True)})


SkiResort.update_forward_refs()
