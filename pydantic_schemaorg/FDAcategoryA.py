from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.DrugPregnancyCategory import DrugPregnancyCategory


class FDAcategoryA(DrugPregnancyCategory):
    """A designation by the US FDA signifying that adequate and well-controlled studies have"
     "failed to demonstrate a risk to the fetus in the first trimester of pregnancy (and there"
     "is no evidence of risk in later trimesters).

    See: https://schema.org/FDAcategoryA
    Model depth: 6
    """
    type_: str = Field("FDAcategoryA", alias='@type')
    

