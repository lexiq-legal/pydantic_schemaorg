from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.AutomotiveBusiness import AutomotiveBusiness


class AutoDealer(AutomotiveBusiness):
    """An car dealership.

    See: https://schema.org/AutoDealer
    Model depth: 5
    """

    type_: str = Field("AutoDealer", const=True, alias="@type")


if TYPE_CHECKING:

    AutoDealer.update_forward_refs()
