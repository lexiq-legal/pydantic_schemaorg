from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.Audience import Audience


class BusinessAudience(Audience):
    """A set of characteristics belonging to businesses, e.g. who compose an item's target"
     "audience.

    See: https://schema.org/BusinessAudience
    Model depth: 4
    """

    type_: str = Field("BusinessAudience", const=True, alias="@type")
    yearsInOperation: "Optional[Union[List[Union[QuantitativeValue, str]], Union[QuantitativeValue, str]]]" = Field(
        None,
        description="The age of the business.",
    )
    numberOfEmployees: "Optional[Union[List[Union[QuantitativeValue, str]], Union[QuantitativeValue, str]]]" = Field(
        None,
        description="The number of employees in an organization e.g. business.",
    )
    yearlyRevenue: "Optional[Union[List[Union[QuantitativeValue, str]], Union[QuantitativeValue, str]]]" = Field(
        None,
        description="The size of the business in annual revenue.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue

    BusinessAudience.update_forward_refs()
