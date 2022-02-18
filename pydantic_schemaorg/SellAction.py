from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.TradeAction import TradeAction


class SellAction(TradeAction):
    """The act of taking money from a buyer in exchange for goods or services rendered. An agent"
     "sells an object, product, or service to a buyer for a price. Reciprocal of BuyAction.

    See: https://schema.org/SellAction
    Model depth: 4
    """
    type_: str = Field(default="SellAction", alias='@type', const=True)
    buyer: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="A sub property of participant. The participant/person/organization that bought the"
     "object.",
    )
    warrantyPromise: Optional[Union[List[Union['WarrantyPromise', str]], 'WarrantyPromise', str]] = Field(
        default=None,
        description="The warranty promise(s) included in the offer.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.WarrantyPromise import WarrantyPromise
