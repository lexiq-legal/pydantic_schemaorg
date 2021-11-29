from pydantic import Field
from pydantic_schema_org.Person import Person
from pydantic_schema_org.Organization import Organization
from typing import Any, Optional, Union, List
from pydantic_schema_org.Service import Service
from pydantic_schema_org.Product import Product
from datetime import datetime
from pydantic_schema_org.StructuredValue import StructuredValue


class OwnershipInfo(StructuredValue):
    """A structured value providing information about when a certain organization or person"
     "owned a certain product.

    See https://schema.org/OwnershipInfo.

    """

    acquiredFrom: Optional[Union[List[Union[Person, Organization]], Union[Person, Organization]]] = Field(
        None,
        description="The organization or person from which the product was acquired.",
    )
    typeOfGood: Optional[Union[List[Union[Service, Product]], Union[Service, Product]]] = Field(
        None,
        description="The product that this structured value is referring to.",
    )
    ownedThrough: Optional[Union[List[datetime], datetime]] = Field(
        None,
        description="The date and time of giving up ownership on the product.",
    )
    ownedFrom: Optional[Union[List[datetime], datetime]] = Field(
        None,
        description="The date and time of obtaining the product.",
    )
    locals().update({"@type": Field("OwnershipInfo", const=True)})


OwnershipInfo.update_forward_refs()
