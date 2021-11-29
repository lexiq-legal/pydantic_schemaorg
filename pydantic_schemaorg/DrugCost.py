from pydantic import Field
from pydantic_schemaorg.DrugCostCategory import DrugCostCategory
from typing import Any, Union, List, Optional
from decimal import Decimal
from pydantic_schemaorg.MedicalEntity import MedicalEntity


class DrugCost(MedicalEntity):
    """The cost per unit of a medical drug. Note that this type is not meant to represent the price"
     "in an offer of a drug for sale; see the Offer type for that. This type will typically be used"
     "to tag wholesale or average retail cost of a drug, or maximum reimbursable cost. Costs"
     "of medical drugs vary widely depending on how and where they are paid for, so while this"
     "type captures some of the variables, costs should be used with caution by consumers of"
     "this schema's markup.

    See https://schema.org/DrugCost.

    """

    costCategory: Optional[Union[List[DrugCostCategory], DrugCostCategory]] = Field(
        None,
        description="The category of cost, such as wholesale, retail, reimbursement cap, etc.",
    )
    drugUnit: Optional[Union[List[str], str]] = Field(
        None,
        description="The unit in which the drug is measured, e.g. '5 mg tablet'.",
    )
    applicableLocation: Any = Field(
        None,
        description="The location in which the status applies.",
    )
    costCurrency: Optional[Union[List[str], str]] = Field(
        None,
        description="The currency (in 3-letter of the drug cost. See: http://en.wikipedia.org/wiki/ISO_4217.",
    )
    costPerUnit: Union[List[Union[Decimal, str, Any]], Union[Decimal, str, Any]] = Field(
        None,
        description="The cost per unit of the drug.",
    )
    costOrigin: Optional[Union[List[str], str]] = Field(
        None,
        description="Additional details to capture the origin of the cost data. For example, 'Medicare Part"
     "B'.",
    )
    locals().update({"@type": Field("DrugCost", const=True)})


DrugCost.update_forward_refs()
