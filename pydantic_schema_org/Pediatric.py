from pydantic import Field
from pydantic_schema_org.MedicalBusiness import MedicalBusiness
from pydantic_schema_org.MedicalSpecialty import MedicalSpecialty


class Pediatric(MedicalBusiness, MedicalSpecialty):
    """A specific branch of medical science that specializes in the care of infants, children"
     "and adolescents.

    See https://schema.org/Pediatric.

    """

    locals().update({"@type": Field("Pediatric", const=True)})


Pediatric.update_forward_refs()
