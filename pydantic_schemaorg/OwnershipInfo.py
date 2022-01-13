from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.StructuredValue import StructuredValue


class OwnershipInfo(StructuredValue):
    """A structured value providing information about when a certain organization or person"
     "owned a certain product.

    See: https://schema.org/OwnershipInfo
    Model depth: 4
    """

    type_: str = Field("OwnershipInfo", const=True, alias="@type")
    acquiredFrom: "Optional[Union[List[Union[Person, Organization, str]], Union[Person, Organization, str]]]" = Field(
        None,
        description="The organization or person from which the product was acquired.",
    )
    typeOfGood: "Optional[Union[List[Union[Product, Service, str]], Union[Product, Service, str]]]" = Field(
        None,
        description="The product that this structured value is referring to.",
    )
    ownedThrough: "Optional[Union[List[Union[datetime, str]], Union[datetime, str]]]" = Field(
        None,
        description="The date and time of giving up ownership on the product.",
    )
    ownedFrom: "Optional[Union[List[Union[datetime, str]], Union[datetime, str]]]" = (
        Field(
            None,
            description="The date and time of obtaining the product.",
        )
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.Person import Person

    from pydantic_schemaorg.Organization import Organization

    from pydantic_schemaorg.Product import Product

    from pydantic_schemaorg.Service import Service

    from datetime import datetime

    OwnershipInfo.update_forward_refs()
