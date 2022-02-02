from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date


from pydantic import Field
from pydantic_schemaorg.WebPage import WebPage


class RealEstateListing(WebPage):
    """A [[RealEstateListing]] is a listing that describes one or more real-estate [[Offer]]s"
     "(whose [[businessFunction]] is typically to lease out, or to sell). The [[RealEstateListing]]"
     "type itself represents the overall listing, as manifested in some [[WebPage]].

    See: https://schema.org/RealEstateListing
    Model depth: 4
    """
    type_: str = Field("RealEstateListing", alias='@type')
    leaseLength: Optional[Union[List[Union['Duration', 'QuantitativeValue', str]], 'Duration', 'QuantitativeValue', str]] = Field(
        None,
        description="Length of the lease for some [[Accommodation]], either particular to some [[Offer]]"
     "or in some cases intrinsic to the property.",
    )
    datePosted: Optional[Union[List[Union[ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]], ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]] = Field(
        None,
        description="Publication date of an online listing.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Duration import Duration
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Date import Date
