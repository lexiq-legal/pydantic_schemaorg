from pydantic import Field
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Gynecologic(MedicalBusiness, MedicalSpecialty):
    """A specific branch of medical science that pertains to the health care of women, particularly"
     "in the diagnosis and treatment of disorders affecting the female reproductive system.

    See https://schema.org/Gynecologic.

    """

    locals().update({"@type": Field("Gynecologic", const=True)})


Gynecologic.update_forward_refs()
