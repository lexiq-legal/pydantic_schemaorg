from pydantic import Field
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Person import Person
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Service import Service
from pydantic_schemaorg.Product import Product
from datetime import datetime
from pydantic_schemaorg.StructuredValue import StructuredValue


class OwnershipInfo(StructuredValue):
    """A structured value providing information about when a certain organization or person"
     "owned a certain product.

    See https://schema.org/OwnershipInfo.

    """

    acquiredFrom: Optional[Union[List[Union[Organization, Person]], Union[Organization, Person]]] = Field(
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
