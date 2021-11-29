from pydantic import Field
from pydantic_schema_org.Duration import Duration
from pydantic_schema_org.QuantitativeValue import QuantitativeValue
from typing import Any, Optional, Union, List
from datetime import datetime, date
from pydantic_schema_org.WebPage import WebPage


class RealEstateListing(WebPage):
    """A [[RealEstateListing]] is a listing that describes one or more real-estate [[Offer]]s"
     "(whose [[businessFunction]] is typically to lease out, or to sell). The [[RealEstateListing]]"
     "type itself represents the overall listing, as manifested in some [[WebPage]].

    See https://schema.org/RealEstateListing.

    """

    leaseLength: Optional[Union[List[Union[Duration, QuantitativeValue]], Union[Duration, QuantitativeValue]]] = Field(
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
