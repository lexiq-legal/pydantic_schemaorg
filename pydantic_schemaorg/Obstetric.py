from pydantic import Field
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Obstetric(MedicalBusiness, MedicalSpecialty):
    """A specific branch of medical science that specializes in the care of women during the"
     "prenatal and postnatal care and with the delivery of the child.

    See https://schema.org/Obstetric.

    """
    type_: str = Field("Obstetric", const=True, alias='@type')
    

Obstetric.update_forward_refs()
