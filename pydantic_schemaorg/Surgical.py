from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Surgical(MedicalSpecialty):
    """A specific branch of medical science that pertains to treating diseases, injuries and"
     "deformities by manual and instrumental means.

    See https://schema.org/Surgical.

    """

    locals().update({"@type": Field("Surgical", const=True)})


Surgical.update_forward_refs()
