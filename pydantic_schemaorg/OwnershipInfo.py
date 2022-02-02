from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date


from pydantic import Field
from pydantic_schemaorg.StructuredValue import StructuredValue


class OwnershipInfo(StructuredValue):
    """A structured value providing information about when a certain organization or person"
     "owned a certain product.

    See: https://schema.org/OwnershipInfo
    Model depth: 4
    """
    type_: str = Field("OwnershipInfo", alias='@type')
    acquiredFrom: Optional[Union[List[Union['Organization', 'Person', str]], 'Organization', 'Person', str]] = Field(
        None,
        description="The organization or person from which the product was acquired.",
    )
    typeOfGood: Optional[Union[List[Union['Service', 'Product', str]], 'Service', 'Product', str]] = Field(
        None,
        description="The product that this structured value is referring to.",
    )
    ownedThrough: Optional[Union[List[Union[ISO8601Date, 'DateTime', str]], ISO8601Date, 'DateTime', str]] = Field(
        None,
        description="The date and time of giving up ownership on the product.",
    )
    ownedFrom: Optional[Union[List[Union[ISO8601Date, 'DateTime', str]], ISO8601Date, 'DateTime', str]] = Field(
        None,
        description="The date and time of obtaining the product.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Service import Service
    from pydantic_schemaorg.Product import Product
    from pydantic_schemaorg.DateTime import DateTime
