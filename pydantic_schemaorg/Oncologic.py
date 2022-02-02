from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness


class Oncologic(MedicalSpecialty, MedicalBusiness):
    """A specific branch of medical science that deals with benign and malignant tumors, including"
     "the study of their development, diagnosis, treatment and prevention.

    See: https://schema.org/Oncologic
    Model depth: 5
    """
    type_: str = Field("Oncologic", alias='@type')
    

