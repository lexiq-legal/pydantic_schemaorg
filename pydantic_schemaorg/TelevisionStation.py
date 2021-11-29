from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class TelevisionStation(LocalBusiness):
    """A television station.

    See https://schema.org/TelevisionStation.

    """

    locals().update({"@type": Field("TelevisionStation", const=True)})


TelevisionStation.update_forward_refs()
