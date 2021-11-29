from pydantic import Field
from pydantic_schemaorg.AutomotiveBusiness import AutomotiveBusiness


class GasStation(AutomotiveBusiness):
    """A gas station.

    See https://schema.org/GasStation.

    """

    locals().update({"@type": Field("GasStation", const=True)})


GasStation.update_forward_refs()
