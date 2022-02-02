from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalTest import MedicalTest


class BloodTest(MedicalTest):
    """A medical test performed on a sample of a patient's blood.

    See: https://schema.org/BloodTest
    Model depth: 4
    """
    type_: str = Field("BloodTest", alias='@type')
    

