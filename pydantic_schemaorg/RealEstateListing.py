from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.WebPage import WebPage


class RealEstateListing(WebPage):
    """A [[RealEstateListing]] is a listing that describes one or more real-estate [[Offer]]s"
     "(whose [[businessFunction]] is typically to lease out, or to sell). The [[RealEstateListing]]"
     "type itself represents the overall listing, as manifested in some [[WebPage]].

    See: https://schema.org/RealEstateListing
    Model depth: 4
    """

    type_: str = Field("RealEstateListing", const=True, alias="@type")
    leaseLength: "Optional[Union[List[Union[QuantitativeValue, Duration, str]], Union[QuantitativeValue, Duration, str]]]" = Field(
        None,
        description="Length of the lease for some [[Accommodation]], either particular to some [[Offer]]"
        "or in some cases intrinsic to the property.",
    )
    datePosted: "Optional[Union[List[Union[datetime, date, str]], Union[datetime, date, str]]]" = Field(
        None,
        description="Publication date of an online listing.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue

    from pydantic_schemaorg.Duration import Duration

    from datetime import date, datetime

    RealEstateListing.update_forward_refs()
