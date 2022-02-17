from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic import StrictBool
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class HealthPlanFormulary(Intangible):
    """For a given health insurance plan, the specification for costs and coverage of prescription"
     "drugs.

    See: https://schema.org/HealthPlanFormulary
    Model depth: 3
    """
    type_: str = Field("HealthPlanFormulary", alias='@type')
    offersPrescriptionByMail: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        default=None,
        description="Whether prescriptions can be delivered by mail.",
    )
    healthPlanDrugTier: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The tier(s) of drugs offered by this formulary or insurance plan.",
    )
    healthPlanCostSharing: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        default=None,
        description="Whether The costs to the patient for services under this network or formulary.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.Text import Text
