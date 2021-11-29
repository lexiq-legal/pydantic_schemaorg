from pydantic import Field, AnyUrl
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Service import Service
from pydantic_schemaorg.Product import Product
from decimal import Decimal
from pydantic_schemaorg.StructuredValue import StructuredValue


class TypeAndQuantityNode(StructuredValue):
    """A structured value indicating the quantity, unit of measurement, and business function"
     "of goods included in a bundle offer.

    See https://schema.org/TypeAndQuantityNode.

    """

    businessFunction: Any = Field(
        None,
        description="The business function (e.g. sell, lease, repair, dispose) of the offer or component"
     "of a bundle (TypeAndQuantityNode). The default is http://purl.org/goodrelations/v1#Sell.",
    )
    typeOfGood: Optional[Union[List[Union[Service, Product]], Union[Service, Product]]] = Field(
        None,
        description="The product that this structured value is referring to.",
    )
    unitText: Optional[Union[List[str], str]] = Field(
        None,
        description="A string or text indicating the unit of measurement. Useful if you cannot provide a standard"
     "unit code for <a href='unitCode'>unitCode</a>.",
    )
    unitCode: Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]] = Field(
        None,
        description="The unit of measurement given using the UN/CEFACT Common Code (3 characters) or a URL."
     "Other codes than the UN/CEFACT Common Code may be used with a prefix followed by a colon.",
    )
    amountOfThisGood: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="The quantity of the goods included in the offer.",
    )
    locals().update({"@type": Field("TypeAndQuantityNode", const=True)})


TypeAndQuantityNode.update_forward_refs()
