from pydantic import Field
from pydantic_schemaorg.DrugPregnancyCategory import DrugPregnancyCategory


class FDAcategoryD(DrugPregnancyCategory):
    """A designation by the US FDA signifying that there is positive evidence of human fetal"
     "risk based on adverse reaction data from investigational or marketing experience or"
     "studies in humans, but potential benefits may warrant use of the drug in pregnant women"
     "despite potential risks.

    See https://schema.org/FDAcategoryD.

    """

    locals().update({"@type": Field("FDAcategoryD", const=True)})


FDAcategoryD.update_forward_refs()
