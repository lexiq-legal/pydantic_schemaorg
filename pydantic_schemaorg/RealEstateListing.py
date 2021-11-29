from pydantic import Field
from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
from pydantic_schemaorg.Duration import Duration
from typing import Any, Union, List, Optional
from datetime import date, datetime
from pydantic_schemaorg.WebPage import WebPage


class RealEstateListing(WebPage):
    """A [[RealEstateListing]] is a listing that describes one or more real-estate [[Offer]]s"
     "(whose [[businessFunction]] is typically to lease out, or to sell). The [[RealEstateListing]]"
     "type itself represents the overall listing, as manifested in some [[WebPage]].

    See https://schema.org/RealEstateListing.

    """

    leaseLength: Optional[Union[List[Union[QuantitativeValue, Duration]], Union[QuantitativeValue, Duration]]] = Field(
        None,
        description="Length of the lease for some [[Accommodation]], either particular to some [[Offer]]"
     "or in some cases intrinsic to the property.",
    )
    datePosted: Optional[Union[List[Union[datetime, date]], Union[datetime, date]]] = Field(
        None,
        description="Publication date of an online listing.",
    )
    locals().update({"@type": Field("RealEstateListing", const=True)})


RealEstateListing.update_forward_refs()
