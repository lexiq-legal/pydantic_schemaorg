from pydantic import Field
from pydantic_schemaorg.TradeAction import TradeAction


class PreOrderAction(TradeAction):
    """An agent orders a (not yet released) object/product/service to be delivered/sent.

    See https://schema.org/PreOrderAction.

    """

    locals().update({"@type": Field("PreOrderAction", const=True)})


PreOrderAction.update_forward_refs()
