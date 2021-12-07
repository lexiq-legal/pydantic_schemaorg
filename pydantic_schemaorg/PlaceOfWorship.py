from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class PlaceOfWorship(CivicStructure):
    """Place of worship, such as a church, synagogue, or mosque.

    See https://schema.org/PlaceOfWorship.

    """
    type_: str = Field("PlaceOfWorship", const=True, alias='@type')
    

PlaceOfWorship.update_forward_refs()
