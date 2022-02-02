from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.DrugCostCategory import DrugCostCategory


class Wholesale(DrugCostCategory):
    """The drug's cost represents the wholesale acquisition cost of the drug.

    See: https://schema.org/Wholesale
    Model depth: 6
    """
    type_: str = Field("Wholesale", alias='@type')
    

