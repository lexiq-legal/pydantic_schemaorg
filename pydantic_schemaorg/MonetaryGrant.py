from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.Grant import Grant


class MonetaryGrant(Grant):
    """A monetary grant.

    See: https://schema.org/MonetaryGrant
    Model depth: 4
    """

    type_: str = Field("MonetaryGrant", const=True, alias="@type")
    funder: "Optional[Union[List[Union[Person, Organization, str]], Union[Person, Organization, str]]]" = Field(
        None,
        description="A person or organization that supports (sponsors) something through some kind of financial"
        "contribution.",
    )
    amount: "Optional[Union[List[Union[Decimal, MonetaryAmount, str]], Union[Decimal, MonetaryAmount, str]]]" = Field(
        None,
        description="The amount of money.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.Person import Person

    from pydantic_schemaorg.Organization import Organization

    from decimal import Decimal

    from pydantic_schemaorg.MonetaryAmount import MonetaryAmount

    MonetaryGrant.update_forward_refs()
