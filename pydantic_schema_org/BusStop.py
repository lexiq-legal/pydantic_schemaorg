from pydantic import Field
from pydantic_schema_org.CivicStructure import CivicStructure


class BusStop(CivicStructure):
    """A bus stop.

    See https://schema.org/BusStop.

    """

    locals().update({"@type": Field("BusStop", const=True)})


BusStop.update_forward_refs()
