from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class Bridge(CivicStructure):
    """A bridge.

    See https://schema.org/Bridge.

    """

    locals().update({"@type": Field("Bridge", const=True)})


Bridge.update_forward_refs()
