from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class PerformingArtsTheater(CivicStructure):
    """A theater or other performing art center.

    See https://schema.org/PerformingArtsTheater.

    """
    type_: str = Field("PerformingArtsTheater", const=True, alias='@type')
    

PerformingArtsTheater.update_forward_refs()
