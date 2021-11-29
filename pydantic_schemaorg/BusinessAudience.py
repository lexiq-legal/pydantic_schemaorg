from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Audience import Audience


class BusinessAudience(Audience):
    """A set of characteristics belonging to businesses, e.g. who compose an item's target"
     "audience.

    See https://schema.org/BusinessAudience.

    """

    yearsInOperation: Any = Field(
        None,
        description="The age of the business.",
    )
    numberOfEmployees: Any = Field(
        None,
        description="The number of employees in an organization e.g. business.",
    )
    yearlyRevenue: Any = Field(
        None,
        description="The size of the business in annual revenue.",
    )
    locals().update({"@type": Field("BusinessAudience", const=True)})


BusinessAudience.update_forward_refs()
