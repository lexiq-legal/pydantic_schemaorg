from pydantic import Field, StrictBool
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Intangible import Intangible


class HealthPlanNetwork(Intangible):
    """A US-style health insurance plan network.

    See https://schema.org/HealthPlanNetwork.

    """

    healthPlanNetworkTier: Optional[Union[List[str], str]] = Field(
        None,
        description="The tier(s) for this network.",
    )
    healthPlanNetworkId: Optional[Union[List[str], str]] = Field(
        None,
        description="Name or unique ID of network. (Networks are often reused across different insurance"
     "plans).",
    )
    healthPlanCostSharing: Optional[Union[List[StrictBool], StrictBool]] = Field(
        None,
        description="Whether The costs to the patient for services under this network or formulary.",
    )
    locals().update({"@type": Field("HealthPlanNetwork", const=True)})


HealthPlanNetwork.update_forward_refs()
