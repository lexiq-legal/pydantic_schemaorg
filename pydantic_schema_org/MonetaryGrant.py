from pydantic import Field
from pydantic_schema_org.Person import Person
from pydantic_schema_org.Organization import Organization
from typing import Any, Optional, Union, List
from decimal import Decimal
from pydantic_schema_org.Grant import Grant


class MonetaryGrant(Grant):
    """A monetary grant.

    See https://schema.org/MonetaryGrant.

    """

    funder: Optional[Union[List[Union[Person, Organization]], Union[Person, Organization]]] = Field(
        None,
        description="A person or organization that supports (sponsors) something through some kind of financial"
     "contribution.",
    )
    amount: Union[List[Union[Decimal, Any]], Union[Decimal, Any]] = Field(
        None,
        description="The amount of money.",
    )
    locals().update({"@type": Field("MonetaryGrant", const=True)})


MonetaryGrant.update_forward_refs()
