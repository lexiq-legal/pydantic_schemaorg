from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class RisksOrComplicationsHealthAspect(HealthAspectEnumeration):
    """Information about the risk factors and possible complications that may follow a topic.

    See https://schema.org/RisksOrComplicationsHealthAspect.

    """

    locals().update({"@type": Field("RisksOrComplicationsHealthAspect", const=True)})


RisksOrComplicationsHealthAspect.update_forward_refs()
