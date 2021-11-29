from pydantic import Field
from pydantic_schema_org.CivicStructure import CivicStructure


class PerformingArtsTheater(CivicStructure):
    """A theater or other performing art center.

    See https://schema.org/PerformingArtsTheater.

    """

    locals().update({"@type": Field("PerformingArtsTheater", const=True)})


PerformingArtsTheater.update_forward_refs()
