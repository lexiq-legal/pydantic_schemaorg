from pydantic import Field
from pydantic_schemaorg.DrugCostCategory import DrugCostCategory


class Retail(DrugCostCategory):
    """The drug's cost represents the retail cost of the drug.

    See https://schema.org/Retail.

    """
    type_: str = Field("Retail", const=True, alias='@type')
    

Retail.update_forward_refs()
