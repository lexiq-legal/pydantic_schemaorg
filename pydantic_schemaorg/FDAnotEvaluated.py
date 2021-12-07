from pydantic import Field
from pydantic_schemaorg.DrugPregnancyCategory import DrugPregnancyCategory


class FDAnotEvaluated(DrugPregnancyCategory):
    """A designation that the drug in question has not been assigned a pregnancy category designation"
     "by the US FDA.

    See https://schema.org/FDAnotEvaluated.

    """
    type_: str = Field("FDAnotEvaluated", const=True, alias='@type')
    

FDAnotEvaluated.update_forward_refs()
