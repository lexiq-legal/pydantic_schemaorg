from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.DrugCostCategory import DrugCostCategory


class Retail(DrugCostCategory):
    """The drug's cost represents the retail cost of the drug.

    See: https://schema.org/Retail
    Model depth: 6
    """
    type_: str = Field("Retail", alias='@type')
    

