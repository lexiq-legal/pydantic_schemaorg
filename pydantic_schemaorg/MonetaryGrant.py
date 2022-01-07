from pydantic import Field
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Person import Person
from typing import List, Optional, Union
from decimal import Decimal
from pydantic_schemaorg.MonetaryAmount import MonetaryAmount
from pydantic_schemaorg.Grant import Grant


class MonetaryGrant(Grant):
    """A monetary grant.

    See https://schema.org/MonetaryGrant.

    """
    type_: str = Field("MonetaryGrant", const=True, alias='@type')
    funder: Optional[Union[List[Union[Organization, Person, str]], Union[Organization, Person, str]]] = Field(
        None,
        description="A person or organization that supports (sponsors) something through some kind of financial"
     "contribution.",
    )
    amount: Optional[Union[List[Union[Decimal, MonetaryAmount, str]], Union[Decimal, MonetaryAmount, str]]] = Field(
        None,
        description="The amount of money.",
    )
    

MonetaryGrant.update_forward_refs()
