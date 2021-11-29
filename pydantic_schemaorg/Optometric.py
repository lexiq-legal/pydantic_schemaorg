from pydantic import Field
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Optometric(MedicalBusiness, MedicalSpecialty):
    """The science or practice of testing visual acuity and prescribing corrective lenses.

    See https://schema.org/Optometric.

    """

    locals().update({"@type": Field("Optometric", const=True)})


Optometric.update_forward_refs()
