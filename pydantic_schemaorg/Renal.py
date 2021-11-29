from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Renal(MedicalSpecialty):
    """A specific branch of medical science that pertains to the study of the kidneys and its"
     "respective disease states.

    See https://schema.org/Renal.

    """

    locals().update({"@type": Field("Renal", const=True)})


Renal.update_forward_refs()
