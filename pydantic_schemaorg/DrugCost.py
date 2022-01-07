from pydantic import Field
from pydantic_schemaorg.DrugCostCategory import DrugCostCategory
from typing import List, Optional, Any, Union
from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
from decimal import Decimal
from pydantic_schemaorg.QualitativeValue import QualitativeValue
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
    type_: str = Field("DrugCost", const=True, alias='@type')
    costCategory: Optional[Union[List[Union[DrugCostCategory, str]], Union[DrugCostCategory, str]]] = Field(
        None,
        description="The category of cost, such as wholesale, retail, reimbursement cap, etc.",
    )
    drugUnit: Optional[Union[List[str], str]] = Field(
        None,
        description="The unit in which the drug is measured, e.g. '5 mg tablet'.",
    )
    applicableLocation: Optional[Union[List[Union[AdministrativeArea, str]], Union[AdministrativeArea, str]]] = Field(
        None,
        description="The location in which the status applies.",
    )
    costCurrency: Optional[Union[List[str], str]] = Field(
        None,
        description="The currency (in 3-letter of the drug cost. See: http://en.wikipedia.org/wiki/ISO_4217.",
    )
    costPerUnit: Optional[Union[List[Union[Decimal, str, QualitativeValue]], Union[Decimal, str, QualitativeValue]]] = Field(
        None,
        description="The cost per unit of the drug.",
    )
    costOrigin: Optional[Union[List[str], str]] = Field(
        None,
        description="Additional details to capture the origin of the cost data. For example, 'Medicare Part"
     "B'.",
    )
    

DrugCost.update_forward_refs()
