from pydantic import Field
from pydantic_schemaorg.TradeAction import TradeAction


class QuoteAction(TradeAction):
    """An agent quotes/estimates/appraises an object/product/service with a price at a location/store.

    See https://schema.org/QuoteAction.

    """

    locals().update({"@type": Field("QuoteAction", const=True)})


QuoteAction.update_forward_refs()
