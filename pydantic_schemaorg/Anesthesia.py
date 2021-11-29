from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Anesthesia(MedicalSpecialty):
    """A specific branch of medical science that pertains to study of anesthetics and their"
     "application.

    See https://schema.org/Anesthesia.

    """

    locals().update({"@type": Field("Anesthesia", const=True)})


Anesthesia.update_forward_refs()
