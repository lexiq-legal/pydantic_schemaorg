from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.RestrictedDiet import RestrictedDiet


class VeganDiet(RestrictedDiet):
    """A diet exclusive of all animal products.

    See: https://schema.org/VeganDiet
    Model depth: 5
    """

    type_: str = Field("VeganDiet", const=True, alias="@type")


if TYPE_CHECKING:

    VeganDiet.update_forward_refs()
