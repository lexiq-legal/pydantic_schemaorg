from pydantic import StrictBool, Field
from typing import List, Optional, Union
from pydantic_schemaorg.Intangible import Intangible


class HealthPlanFormulary(Intangible):
    """For a given health insurance plan, the specification for costs and coverage of prescription"
     "drugs.

    See https://schema.org/HealthPlanFormulary.

    """
    type_: str = Field("HealthPlanFormulary", const=True, alias='@type')
    offersPrescriptionByMail: Optional[Union[List[Union[StrictBool, str]], Union[StrictBool, str]]] = Field(
        None,
        description="Whether prescriptions can be delivered by mail.",
    )
    healthPlanDrugTier: Optional[Union[List[str], str]] = Field(
        None,
        description="The tier(s) of drugs offered by this formulary or insurance plan.",
    )
    healthPlanCostSharing: Optional[Union[List[Union[StrictBool, str]], Union[StrictBool, str]]] = Field(
        None,
        description="Whether The costs to the patient for services under this network or formulary.",
    )
    

HealthPlanFormulary.update_forward_refs()
