from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration


class DrugPregnancyCategory(MedicalEnumeration):
    """Categories that represent an assessment of the risk of fetal injury due to a drug or pharmaceutical"
     "used as directed by the mother during pregnancy.

    See: https://schema.org/DrugPregnancyCategory
    Model depth: 5
    """
    type_: str = Field("DrugPregnancyCategory", alias='@type')
    

