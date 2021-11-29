from pydantic import Field
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Person import Person
from typing import Any, Union, List, Optional
from decimal import Decimal
from pydantic_schemaorg.Grant import Grant


class MonetaryGrant(Grant):
    """A monetary grant.

    See https://schema.org/MonetaryGrant.

    """

    funder: Optional[Union[List[Union[Organization, Person]], Union[Organization, Person]]] = Field(
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
