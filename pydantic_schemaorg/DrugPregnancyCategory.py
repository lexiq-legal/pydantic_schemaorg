from pydantic import Field
from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration


class DrugPregnancyCategory(MedicalEnumeration):
    """Categories that represent an assessment of the risk of fetal injury due to a drug or pharmaceutical"
     "used as directed by the mother during pregnancy.

    See https://schema.org/DrugPregnancyCategory.

    """

    locals().update({"@type": Field("DrugPregnancyCategory", const=True)})


DrugPregnancyCategory.update_forward_refs()
