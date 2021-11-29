from pydantic import Field
from datetime import date, datetime
from typing import Any, Union, List, Optional
from pydantic_schemaorg.MerchantReturnEnumeration import MerchantReturnEnumeration
from pydantic_schemaorg.Intangible import Intangible


class MerchantReturnPolicySeasonalOverride(Intangible):
    """A seasonal override of a return policy, for example used for holidays.

    See https://schema.org/MerchantReturnPolicySeasonalOverride.

    """

    merchantReturnDays: Optional[Union[List[Union[datetime, int, date]], Union[datetime, int, date]]] = Field(
        None,
        description="Specifies either a fixed return date or the number of days (from the delivery date) that"
     "a product can be returned. Used when the [[returnPolicyCategory]] property is specified"
     "as [[MerchantReturnFiniteReturnWindow]].",
    )
    endDate: Optional[Union[List[Union[datetime, date]], Union[datetime, date]]] = Field(
        None,
        description="The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    returnPolicyCategory: Optional[Union[List[MerchantReturnEnumeration], MerchantReturnEnumeration]] = Field(
        None,
        description="Specifies an applicable return policy (from an enumeration).",
    )
    startDate: Optional[Union[List[Union[datetime, date]], Union[datetime, date]]] = Field(
        None,
        description="The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    locals().update({"@type": Field("MerchantReturnPolicySeasonalOverride", const=True)})


MerchantReturnPolicySeasonalOverride.update_forward_refs()
