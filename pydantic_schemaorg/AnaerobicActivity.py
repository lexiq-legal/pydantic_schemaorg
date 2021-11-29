from pydantic import Field
from pydantic_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory


class AnaerobicActivity(PhysicalActivityCategory):
    """Physical activity that is of high-intensity which utilizes the anaerobic metabolism"
     "of the body.

    See https://schema.org/AnaerobicActivity.

    """

    locals().update({"@type": Field("AnaerobicActivity", const=True)})


AnaerobicActivity.update_forward_refs()
