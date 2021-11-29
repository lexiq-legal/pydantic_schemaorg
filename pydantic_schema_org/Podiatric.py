from pydantic import Field
from pydantic_schema_org.MedicalBusiness import MedicalBusiness
from pydantic_schema_org.MedicalSpecialty import MedicalSpecialty


class Podiatric(MedicalBusiness, MedicalSpecialty):
    """Podiatry is the care of the human foot, especially the diagnosis and treatment of foot"
     "disorders.

    See https://schema.org/Podiatric.

    """

    locals().update({"@type": Field("Podiatric", const=True)})


Podiatric.update_forward_refs()
