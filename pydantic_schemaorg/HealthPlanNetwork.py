from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from pydantic import StrictBool


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class HealthPlanNetwork(Intangible):
    """A US-style health insurance plan network.

    See: https://schema.org/HealthPlanNetwork
    Model depth: 3
    """
    type_: str = Field("HealthPlanNetwork", alias='@type')
    healthPlanNetworkTier: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The tier(s) for this network.",
    )
    healthPlanNetworkId: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Name or unique ID of network. (Networks are often reused across different insurance"
     "plans).",
    )
    healthPlanCostSharing: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        None,
        description="Whether The costs to the patient for services under this network or formulary.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Boolean import Boolean
