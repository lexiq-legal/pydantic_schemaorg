from pydantic import Field
from pydantic_schema_org.SportsActivityLocation import SportsActivityLocation


class TennisComplex(SportsActivityLocation):
    """A tennis complex.

    See https://schema.org/TennisComplex.

    """

    locals().update({"@type": Field("TennisComplex", const=True)})


TennisComplex.update_forward_refs()
