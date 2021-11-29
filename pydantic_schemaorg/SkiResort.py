from pydantic import Field
from pydantic_schemaorg.Resort import Resort
from pydantic_schemaorg.SportsActivityLocation import SportsActivityLocation


class SkiResort(Resort, SportsActivityLocation):
    """A ski resort.

    See https://schema.org/SkiResort.

    """

    locals().update({"@type": Field("SkiResort", const=True)})


SkiResort.update_forward_refs()
