from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Pathology(MedicalSpecialty):
    """A specific branch of medical science that is concerned with the study of the cause, origin"
     "and nature of a disease state, including its consequences as a result of manifestation"
     "of the disease. In clinical care, the term is used to designate a branch of medicine using"
     "laboratory tests to diagnose and determine the prognostic significance of illness.

    See https://schema.org/Pathology.

    """

    locals().update({"@type": Field("Pathology", const=True)})


Pathology.update_forward_refs()
