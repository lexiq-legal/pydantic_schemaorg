from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.RestrictedDiet import RestrictedDiet


class LowSaltDiet(RestrictedDiet):
    """A diet focused on reduced sodium intake.

    See: https://schema.org/LowSaltDiet
    Model depth: 5
    """

    type_: str = Field("LowSaltDiet", const=True, alias="@type")


if TYPE_CHECKING:

    LowSaltDiet.update_forward_refs()
