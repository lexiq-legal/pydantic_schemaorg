from pydantic import Field
from pydantic_schema_org.PhysicalActivityCategory import PhysicalActivityCategory


class OccupationalActivity(PhysicalActivityCategory):
    """Any physical activity engaged in for job-related purposes. Examples may include waiting"
     "tables, maid service, carrying a mailbag, picking fruits or vegetables, construction"
     "work, etc.

    See https://schema.org/OccupationalActivity.

    """

    locals().update({"@type": Field("OccupationalActivity", const=True)})


OccupationalActivity.update_forward_refs()
