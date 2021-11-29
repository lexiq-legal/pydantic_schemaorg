from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness


class Psychiatric(MedicalSpecialty, MedicalBusiness):
    """A specific branch of medical science that is concerned with the study, treatment, and"
     "prevention of mental illness, using both medical and psychological therapies.

    See https://schema.org/Psychiatric.

    """

    locals().update({"@type": Field("Psychiatric", const=True)})


Psychiatric.update_forward_refs()
