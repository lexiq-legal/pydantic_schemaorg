from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.Intangible import Intangible


class HealthPlanCostSharingSpecification(Intangible):
    """A description of costs to the patient under a given network or formulary.

    See: https://schema.org/HealthPlanCostSharingSpecification
    Model depth: 3
    """

    type_: str = Field("HealthPlanCostSharingSpecification", const=True, alias="@type")
    healthPlanCoinsuranceOption: "Optional[Union[List[str], str]]" = Field(
        None,
        description="Whether the coinsurance applies before or after deductible, etc. TODO: Is this a closed"
        "set?",
    )
    healthPlanPharmacyCategory: "Optional[Union[List[str], str]]" = Field(
        None,
        description="The category or type of pharmacy associated with this cost sharing.",
    )
    healthPlanCopay: "Optional[Union[List[Union[PriceSpecification, str]], Union[PriceSpecification, str]]]" = Field(
        None,
        description="Whether The copay amount.",
    )
    healthPlanCopayOption: "Optional[Union[List[str], str]]" = Field(
        None,
        description="Whether the copay is before or after deductible, etc. TODO: Is this a closed set?",
    )
    healthPlanCoinsuranceRate: "Optional[Union[List[Union[Decimal, str]], Union[Decimal, str]]]" = Field(
        None,
        description="Whether The rate of coinsurance expressed as a number between 0.0 and 1.0.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.PriceSpecification import PriceSpecification

    from decimal import Decimal

    HealthPlanCostSharingSpecification.update_forward_refs()
