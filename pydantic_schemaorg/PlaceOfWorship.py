from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class PlaceOfWorship(CivicStructure):
    """Place of worship, such as a church, synagogue, or mosque.

    See https://schema.org/PlaceOfWorship.

    """

    locals().update({"@type": Field("PlaceOfWorship", const=True)})


PlaceOfWorship.update_forward_refs()
