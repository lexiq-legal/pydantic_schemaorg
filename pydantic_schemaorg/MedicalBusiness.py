from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class MedicalBusiness(LocalBusiness):
    """A particular physical or virtual business of an organization for medical purposes."
     "Examples of MedicalBusiness include differents business run by health professionals.

    See: https://schema.org/MedicalBusiness
    Model depth: 4
    """
    type_: str = Field("MedicalBusiness", alias='@type')
    

