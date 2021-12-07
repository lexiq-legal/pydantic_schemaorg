from pydantic import Field
from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration


class DrugCostCategory(MedicalEnumeration):
    """Enumerated categories of medical drug costs.

    See https://schema.org/DrugCostCategory.

    """
    type_: str = Field("DrugCostCategory", const=True, alias='@type')
    

DrugCostCategory.update_forward_refs()
