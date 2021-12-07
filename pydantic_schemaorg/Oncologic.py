from pydantic import Field
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Oncologic(MedicalBusiness, MedicalSpecialty):
    """A specific branch of medical science that deals with benign and malignant tumors, including"
     "the study of their development, diagnosis, treatment and prevention.

    See https://schema.org/Oncologic.

    """
    type_: str = Field("Oncologic", const=True, alias='@type')
    

Oncologic.update_forward_refs()
