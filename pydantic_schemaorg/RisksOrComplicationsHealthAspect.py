from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class RisksOrComplicationsHealthAspect(HealthAspectEnumeration):
    """Information about the risk factors and possible complications that may follow a topic.

    See https://schema.org/RisksOrComplicationsHealthAspect.

    """
    type_: str = Field("RisksOrComplicationsHealthAspect", const=True, alias='@type')
    

RisksOrComplicationsHealthAspect.update_forward_refs()
