from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Genetic(MedicalSpecialty):
    """A specific branch of medical science that pertains to hereditary transmission and the"
     "variation of inherited characteristics and disorders.

    See https://schema.org/Genetic.

    """

    locals().update({"@type": Field("Genetic", const=True)})


Genetic.update_forward_refs()
