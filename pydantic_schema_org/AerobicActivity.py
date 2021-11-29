from pydantic import Field
from pydantic_schema_org.PhysicalActivityCategory import PhysicalActivityCategory


class AerobicActivity(PhysicalActivityCategory):
    """Physical activity of relatively low intensity that depends primarily on the aerobic"
     "energy-generating process; during activity, the aerobic metabolism uses oxygen to"
     "adequately meet energy demands during exercise.

    See https://schema.org/AerobicActivity.

    """

    locals().update({"@type": Field("AerobicActivity", const=True)})


AerobicActivity.update_forward_refs()
