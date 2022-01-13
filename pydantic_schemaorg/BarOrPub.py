from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.FoodEstablishment import FoodEstablishment


class BarOrPub(FoodEstablishment):
    """A bar or pub.

    See: https://schema.org/BarOrPub
    Model depth: 5
    """

    type_: str = Field("BarOrPub", const=True, alias="@type")


if TYPE_CHECKING:

    BarOrPub.update_forward_refs()
