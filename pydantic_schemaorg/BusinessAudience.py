from pydantic import Field
from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
from typing import List, Optional, Union
from pydantic_schemaorg.Audience import Audience


class BusinessAudience(Audience):
    """A set of characteristics belonging to businesses, e.g. who compose an item's target"
     "audience.

    See https://schema.org/BusinessAudience.

    """
    type_: str = Field("BusinessAudience", const=True, alias='@type')
    yearsInOperation: Optional[Union[List[Union[QuantitativeValue, str]], Union[QuantitativeValue, str]]] = Field(
        None,
        description="The age of the business.",
    )
    numberOfEmployees: Optional[Union[List[Union[QuantitativeValue, str]], Union[QuantitativeValue, str]]] = Field(
        None,
        description="The number of employees in an organization e.g. business.",
    )
    yearlyRevenue: Optional[Union[List[Union[QuantitativeValue, str]], Union[QuantitativeValue, str]]] = Field(
        None,
        description="The size of the business in annual revenue.",
    )
    

BusinessAudience.update_forward_refs()
