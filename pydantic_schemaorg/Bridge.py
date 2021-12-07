from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class Bridge(CivicStructure):
    """A bridge.

    See https://schema.org/Bridge.

    """
    type_: str = Field("Bridge", const=True, alias='@type')
    

Bridge.update_forward_refs()
