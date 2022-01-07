from pydantic import Field
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Person import Person
from typing import List, Optional, Union
from pydantic_schemaorg.Product import Product
from pydantic_schemaorg.Service import Service
from datetime import datetime
from pydantic_schemaorg.StructuredValue import StructuredValue


class OwnershipInfo(StructuredValue):
    """A structured value providing information about when a certain organization or person"
     "owned a certain product.

    See https://schema.org/OwnershipInfo.

    """
    type_: str = Field("OwnershipInfo", const=True, alias='@type')
    acquiredFrom: Optional[Union[List[Union[Organization, Person, str]], Union[Organization, Person, str]]] = Field(
        None,
        description="The organization or person from which the product was acquired.",
    )
    typeOfGood: Optional[Union[List[Union[Product, Service, str]], Union[Product, Service, str]]] = Field(
        None,
        description="The product that this structured value is referring to.",
    )
    ownedThrough: Optional[Union[List[Union[datetime, str]], Union[datetime, str]]] = Field(
        None,
        description="The date and time of giving up ownership on the product.",
    )
    ownedFrom: Optional[Union[List[Union[datetime, str]], Union[datetime, str]]] = Field(
        None,
        description="The date and time of obtaining the product.",
    )
    

OwnershipInfo.update_forward_refs()
