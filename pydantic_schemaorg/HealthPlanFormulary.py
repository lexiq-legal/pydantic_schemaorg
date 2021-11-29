from pydantic import Field, StrictBool
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Intangible import Intangible


class HealthPlanFormulary(Intangible):
    """For a given health insurance plan, the specification for costs and coverage of prescription"
     "drugs.

    See https://schema.org/HealthPlanFormulary.

    """

    offersPrescriptionByMail: Optional[Union[List[StrictBool], StrictBool]] = Field(
        None,
        description="Whether prescriptions can be delivered by mail.",
    )
    healthPlanDrugTier: Optional[Union[List[str], str]] = Field(
        None,
        description="The tier(s) of drugs offered by this formulary or insurance plan.",
    )
    healthPlanCostSharing: Optional[Union[List[StrictBool], StrictBool]] = Field(
        None,
        description="Whether The costs to the patient for services under this network or formulary.",
    )
    locals().update({"@type": Field("HealthPlanFormulary", const=True)})


HealthPlanFormulary.update_forward_refs()
