from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from datetime import date, datetime


from pydantic import Field
from pydantic_schemaorg.WebPage import WebPage


class RealEstateListing(WebPage):
    """A [[RealEstateListing]] is a listing that describes one or more real-estate [[Offer]]s"
     "(whose [[businessFunction]] is typically to lease out, or to sell). The [[RealEstateListing]]"
     "type itself represents the overall listing, as manifested in some [[WebPage]].

    See: https://schema.org/RealEstateListing
    Model depth: 4
    """
    type_: str = Field(default="RealEstateListing", alias='@type', const=True)
    leaseLength: Optional[Union[List[Union['Duration', 'QuantitativeValue', str]], 'Duration', 'QuantitativeValue', str]] = Field(
        default=None,
        description="Length of the lease for some [[Accommodation]], either particular to some [[Offer]]"
     "or in some cases intrinsic to the property.",
    )
    datePosted: Optional[Union[List[Union[datetime, 'DateTime', date, 'Date', str]], datetime, 'DateTime', date, 'Date', str]] = Field(
        default=None,
        description="Publication date of an online listing.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Duration import Duration
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Date import Date
