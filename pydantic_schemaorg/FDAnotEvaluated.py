from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.DrugPregnancyCategory import DrugPregnancyCategory


class FDAnotEvaluated(DrugPregnancyCategory):
    """A designation that the drug in question has not been assigned a pregnancy category designation"
     "by the US FDA.

    See: https://schema.org/FDAnotEvaluated
    Model depth: 6
    """
    type_: str = Field("FDAnotEvaluated", alias='@type')
    

