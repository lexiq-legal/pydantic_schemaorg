from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration


class DrugCostCategory(MedicalEnumeration):
    """Enumerated categories of medical drug costs.

    See: https://schema.org/DrugCostCategory
    Model depth: 5
    """
    type_: str = Field("DrugCostCategory", alias='@type')
    

