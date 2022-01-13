from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.LocalBusiness import LocalBusiness


class AutomotiveBusiness(LocalBusiness):
    """Car repair, sales, or parts.

    See: https://schema.org/AutomotiveBusiness
    Model depth: 4
    """

    type_: str = Field("AutomotiveBusiness", const=True, alias="@type")


if TYPE_CHECKING:

    AutomotiveBusiness.update_forward_refs()
