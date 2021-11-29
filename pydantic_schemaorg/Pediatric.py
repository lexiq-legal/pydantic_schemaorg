from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness


class Pediatric(MedicalSpecialty, MedicalBusiness):
    """A specific branch of medical science that specializes in the care of infants, children"
     "and adolescents.

    See https://schema.org/Pediatric.

    """

    locals().update({"@type": Field("Pediatric", const=True)})


Pediatric.update_forward_refs()
