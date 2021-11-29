from pydantic import Field
from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration


class DrugCostCategory(MedicalEnumeration):
    """Enumerated categories of medical drug costs.

    See https://schema.org/DrugCostCategory.

    """

    locals().update({"@type": Field("DrugCostCategory", const=True)})


DrugCostCategory.update_forward_refs()
