from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness


class Geriatric(MedicalSpecialty, MedicalBusiness):
    """A specific branch of medical science that is concerned with the diagnosis and treatment"
     "of diseases, debilities and provision of care to the aged.

    See https://schema.org/Geriatric.

    """

    locals().update({"@type": Field("Geriatric", const=True)})


Geriatric.update_forward_refs()
