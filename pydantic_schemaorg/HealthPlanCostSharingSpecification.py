from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from decimal import Decimal


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class HealthPlanCostSharingSpecification(Intangible):
    """A description of costs to the patient under a given network or formulary.

    See: https://schema.org/HealthPlanCostSharingSpecification
    Model depth: 3
    """
    type_: str = Field("HealthPlanCostSharingSpecification", alias='@type')
    healthPlanCoinsuranceOption: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Whether the coinsurance applies before or after deductible, etc. TODO: Is this a closed"
     "set?",
    )
    healthPlanPharmacyCategory: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The category or type of pharmacy associated with this cost sharing.",
    )
    healthPlanCopay: Optional[Union[List[Union['PriceSpecification', str]], 'PriceSpecification', str]] = Field(
        None,
        description="Whether The copay amount.",
    )
    healthPlanCopayOption: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Whether the copay is before or after deductible, etc. TODO: Is this a closed set?",
    )
    healthPlanCoinsuranceRate: Optional[Union[List[Union[Decimal, 'Number', str]], Decimal, 'Number', str]] = Field(
        None,
        description="Whether The rate of coinsurance expressed as a number between 0.0 and 1.0.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.PriceSpecification import PriceSpecification
    from pydantic_schemaorg.Number import Number
