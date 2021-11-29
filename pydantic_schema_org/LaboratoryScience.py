from pydantic import Field
from pydantic_schema_org.MedicalSpecialty import MedicalSpecialty


class LaboratoryScience(MedicalSpecialty):
    """A medical science pertaining to chemical, hematological, immunologic, microscopic,"
     "or bacteriological diagnostic analyses or research.

    See https://schema.org/LaboratoryScience.

    """

    locals().update({"@type": Field("LaboratoryScience", const=True)})


LaboratoryScience.update_forward_refs()
