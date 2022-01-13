from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.RestrictedDiet import RestrictedDiet


class VegetarianDiet(RestrictedDiet):
    """A diet exclusive of animal meat.

    See: https://schema.org/VegetarianDiet
    Model depth: 5
    """

    type_: str = Field("VegetarianDiet", const=True, alias="@type")


if TYPE_CHECKING:

    VegetarianDiet.update_forward_refs()
