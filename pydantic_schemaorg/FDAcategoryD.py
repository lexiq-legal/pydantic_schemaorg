from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.DrugPregnancyCategory import DrugPregnancyCategory


class FDAcategoryD(DrugPregnancyCategory):
    """A designation by the US FDA signifying that there is positive evidence of human fetal"
     "risk based on adverse reaction data from investigational or marketing experience or"
     "studies in humans, but potential benefits may warrant use of the drug in pregnant women"
     "despite potential risks.

    See: https://schema.org/FDAcategoryD
    Model depth: 6
    """

    type_: str = Field("FDAcategoryD", const=True, alias="@type")


if TYPE_CHECKING:

    FDAcategoryD.update_forward_refs()
