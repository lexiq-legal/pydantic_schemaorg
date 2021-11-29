from pydantic import Field
from pydantic_schemaorg.DrugPregnancyCategory import DrugPregnancyCategory


class FDAcategoryX(DrugPregnancyCategory):
    """A designation by the US FDA signifying that studies in animals or humans have demonstrated"
     "fetal abnormalities and/or there is positive evidence of human fetal risk based on adverse"
     "reaction data from investigational or marketing experience, and the risks involved"
     "in use of the drug in pregnant women clearly outweigh potential benefits.

    See https://schema.org/FDAcategoryX.

    """

    locals().update({"@type": Field("FDAcategoryX", const=True)})


FDAcategoryX.update_forward_refs()
