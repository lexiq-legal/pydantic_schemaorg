from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.Intangible import Intangible


class MerchantReturnPolicySeasonalOverride(Intangible):
    """A seasonal override of a return policy, for example used for holidays.

    See: https://schema.org/MerchantReturnPolicySeasonalOverride
    Model depth: 3
    """

    type_: str = Field(
        "MerchantReturnPolicySeasonalOverride", const=True, alias="@type"
    )
    merchantReturnDays: "Optional[Union[List[Union[int, datetime, date, str]], Union[int, datetime, date, str]]]" = Field(
        None,
        description="Specifies either a fixed return date or the number of days (from the delivery date) that"
        "a product can be returned. Used when the [[returnPolicyCategory]] property is specified"
        "as [[MerchantReturnFiniteReturnWindow]].",
    )
    endDate: "Optional[Union[List[Union[datetime, date, str]], Union[datetime, date, str]]]" = Field(
        None,
        description="The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    returnPolicyCategory: "Optional[Union[List[Union[MerchantReturnEnumeration, str]], Union[MerchantReturnEnumeration, str]]]" = Field(
        None,
        description="Specifies an applicable return policy (from an enumeration).",
    )
    startDate: "Optional[Union[List[Union[datetime, date, str]], Union[datetime, date, str]]]" = Field(
        None,
        description="The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )


if TYPE_CHECKING:

    from datetime import date, datetime

    from pydantic_schemaorg.MerchantReturnEnumeration import MerchantReturnEnumeration

    MerchantReturnPolicySeasonalOverride.update_forward_refs()
