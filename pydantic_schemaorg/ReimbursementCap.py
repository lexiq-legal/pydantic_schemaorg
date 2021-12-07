from pydantic import Field
from pydantic_schemaorg.DrugCostCategory import DrugCostCategory


class ReimbursementCap(DrugCostCategory):
    """The drug's cost represents the maximum reimbursement paid by an insurer for the drug.

    See https://schema.org/ReimbursementCap.

    """
    type_: str = Field("ReimbursementCap", const=True, alias='@type')
    

ReimbursementCap.update_forward_refs()
