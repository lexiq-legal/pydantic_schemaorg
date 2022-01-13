from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.LocalBusiness import LocalBusiness


class RecyclingCenter(LocalBusiness):
    """A recycling center.

    See: https://schema.org/RecyclingCenter
    Model depth: 4
    """

    type_: str = Field("RecyclingCenter", const=True, alias="@type")


if TYPE_CHECKING:

    RecyclingCenter.update_forward_refs()
