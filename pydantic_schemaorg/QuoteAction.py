from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.TradeAction import TradeAction


class QuoteAction(TradeAction):
    """An agent quotes/estimates/appraises an object/product/service with a price at a location/store.

    See: https://schema.org/QuoteAction
    Model depth: 4
    """
    type_: str = Field("QuoteAction", alias='@type')
    

