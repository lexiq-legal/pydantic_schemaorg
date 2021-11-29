from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness


class Optometric(MedicalSpecialty, MedicalBusiness):
    """The science or practice of testing visual acuity and prescribing corrective lenses.

    See https://schema.org/Optometric.

    """

    locals().update({"@type": Field("Optometric", const=True)})


Optometric.update_forward_refs()
