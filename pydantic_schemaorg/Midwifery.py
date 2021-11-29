from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness


class Midwifery(MedicalSpecialty, MedicalBusiness):
    """A nurse-like health profession that deals with pregnancy, childbirth, and the postpartum"
     "period (including care of the newborn), besides sexual and reproductive health of women"
     "throughout their lives.

    See https://schema.org/Midwifery.

    """

    locals().update({"@type": Field("Midwifery", const=True)})


Midwifery.update_forward_refs()
