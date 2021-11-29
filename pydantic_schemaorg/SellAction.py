from pydantic import Field
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Person import Person
from typing import Any, Union, List, Optional
from pydantic_schemaorg.TradeAction import TradeAction


class SellAction(TradeAction):
    """The act of taking money from a buyer in exchange for goods or services rendered. An agent"
     "sells an object, product, or service to a buyer for a price. Reciprocal of BuyAction.

    See https://schema.org/SellAction.

    """

    buyer: Optional[Union[List[Union[Organization, Person]], Union[Organization, Person]]] = Field(
        None,
        description="A sub property of participant. The participant/person/organization that bought the"
     "object.",
    )
    warrantyPromise: Any = Field(
        None,
        description="The warranty promise(s) included in the offer.",
    )
    locals().update({"@type": Field("SellAction", const=True)})


SellAction.update_forward_refs()
