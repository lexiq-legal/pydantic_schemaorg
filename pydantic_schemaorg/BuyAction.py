from pydantic import Field
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Person import Person
from typing import Any, Union, List, Optional
from pydantic_schemaorg.WarrantyPromise import WarrantyPromise
from pydantic_schemaorg.TradeAction import TradeAction


class BuyAction(TradeAction):
    """The act of giving money to a seller in exchange for goods or services rendered. An agent"
     "buys an object, product, or service from a seller for a price. Reciprocal of SellAction.

    See https://schema.org/BuyAction.

    """

    vendor: Optional[Union[List[Union[Organization, Person]], Union[Organization, Person]]] = Field(
        None,
        description="'vendor' is an earlier term for 'seller'.",
    )
    seller: Optional[Union[List[Union[Organization, Person]], Union[Organization, Person]]] = Field(
        None,
        description="An entity which offers (sells / leases / lends / loans) the services / goods. A seller may"
     "also be a provider.",
    )
    warrantyPromise: Optional[Union[List[WarrantyPromise], WarrantyPromise]] = Field(
        None,
        description="The warranty promise(s) included in the offer.",
    )
    locals().update({"@type": Field("BuyAction", const=True)})


BuyAction.update_forward_refs()
