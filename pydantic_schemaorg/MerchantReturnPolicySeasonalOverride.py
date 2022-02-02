from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class MerchantReturnPolicySeasonalOverride(Intangible):
    """A seasonal override of a return policy, for example used for holidays.

    See: https://schema.org/MerchantReturnPolicySeasonalOverride
    Model depth: 3
    """
    type_: str = Field("MerchantReturnPolicySeasonalOverride", alias='@type')
    merchantReturnDays: Optional[Union[List[Union[int, 'Integer', ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]], int, 'Integer', ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]] = Field(
        None,
        description="Specifies either a fixed return date or the number of days (from the delivery date) that"
     "a product can be returned. Used when the [[returnPolicyCategory]] property is specified"
     "as [[MerchantReturnFiniteReturnWindow]].",
    )
    endDate: Optional[Union[List[Union[ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]], ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]] = Field(
        None,
        description="The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    returnPolicyCategory: Optional[Union[List[Union['MerchantReturnEnumeration', str]], 'MerchantReturnEnumeration', str]] = Field(
        None,
        description="Specifies an applicable return policy (from an enumeration).",
    )
    startDate: Optional[Union[List[Union[ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]], ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]] = Field(
        None,
        description="The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.MerchantReturnEnumeration import MerchantReturnEnumeration
