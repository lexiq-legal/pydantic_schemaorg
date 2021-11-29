from pydantic import Field
from pydantic_schemaorg.DrugPregnancyCategory import DrugPregnancyCategory


class FDAnotEvaluated(DrugPregnancyCategory):
    """A designation that the drug in question has not been assigned a pregnancy category designation"
     "by the US FDA.

    See https://schema.org/FDAnotEvaluated.

    """

    locals().update({"@type": Field("FDAnotEvaluated", const=True)})


FDAnotEvaluated.update_forward_refs()
