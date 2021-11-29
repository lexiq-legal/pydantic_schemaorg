from pydantic import Field
from pydantic_schema_org.MedicalBusiness import MedicalBusiness
from pydantic_schema_org.MedicalSpecialty import MedicalSpecialty


class Obstetric(MedicalBusiness, MedicalSpecialty):
    """A specific branch of medical science that specializes in the care of women during the"
     "prenatal and postnatal care and with the delivery of the child.

    See https://schema.org/Obstetric.

    """

    locals().update({"@type": Field("Obstetric", const=True)})


Obstetric.update_forward_refs()
