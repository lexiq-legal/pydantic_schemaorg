from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.DrugPregnancyCategory import DrugPregnancyCategory


class FDAcategoryB(DrugPregnancyCategory):
    """A designation by the US FDA signifying that animal reproduction studies have failed"
     "to demonstrate a risk to the fetus and there are no adequate and well-controlled studies"
     "in pregnant women.

    See: https://schema.org/FDAcategoryB
    Model depth: 6
    """
    type_: str = Field("FDAcategoryB", alias='@type')
    

