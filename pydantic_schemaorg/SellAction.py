from pydantic import Field
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Person import Person
from typing import List, Optional, Union
from pydantic_schemaorg.WarrantyPromise import WarrantyPromise
from pydantic_schemaorg.TradeAction import TradeAction


class SellAction(TradeAction):
    """The act of taking money from a buyer in exchange for goods or services rendered. An agent"
     "sells an object, product, or service to a buyer for a price. Reciprocal of BuyAction.

    See https://schema.org/SellAction.

    """
    type_: str = Field("SellAction", const=True, alias='@type')
    buyer: Optional[Union[List[Union[Organization, Person, str]], Union[Organization, Person, str]]] = Field(
        None,
        description="A sub property of participant. The participant/person/organization that bought the"
     "object.",
    )
    warrantyPromise: Optional[Union[List[Union[WarrantyPromise, str]], Union[WarrantyPromise, str]]] = Field(
        None,
        description="The warranty promise(s) included in the offer.",
    )
    

SellAction.update_forward_refs()
