from pydantic import Field
from pydantic_schemaorg.Duration import Duration
from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
from typing import List, Optional, Union
from datetime import datetime, date
from pydantic_schemaorg.WebPage import WebPage


class RealEstateListing(WebPage):
    """A [[RealEstateListing]] is a listing that describes one or more real-estate [[Offer]]s"
     "(whose [[businessFunction]] is typically to lease out, or to sell). The [[RealEstateListing]]"
     "type itself represents the overall listing, as manifested in some [[WebPage]].

    See https://schema.org/RealEstateListing.

    """
    type_: str = Field("RealEstateListing", const=True, alias='@type')
    leaseLength: Optional[Union[List[Union[Duration, QuantitativeValue, str]], Union[Duration, QuantitativeValue, str]]] = Field(
        None,
        description="Length of the lease for some [[Accommodation]], either particular to some [[Offer]]"
     "or in some cases intrinsic to the property.",
    )
    datePosted: Optional[Union[List[Union[datetime, date, str]], Union[datetime, date, str]]] = Field(
        None,
        description="Publication date of an online listing.",
    )
    

RealEstateListing.update_forward_refs()
