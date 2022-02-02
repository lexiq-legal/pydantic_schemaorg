from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.DrugPrescriptionStatus import DrugPrescriptionStatus


class PrescriptionOnly(DrugPrescriptionStatus):
    """Available by prescription only.

    See: https://schema.org/PrescriptionOnly
    Model depth: 6
    """
    type_: str = Field("PrescriptionOnly", alias='@type')
    

