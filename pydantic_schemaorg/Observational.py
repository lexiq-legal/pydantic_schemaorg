from pydantic import Field
from pydantic_schemaorg.MedicalObservationalStudyDesign import MedicalObservationalStudyDesign


class Observational(MedicalObservationalStudyDesign):
    """An observational study design.

    See https://schema.org/Observational.

    """

    locals().update({"@type": Field("Observational", const=True)})


Observational.update_forward_refs()
