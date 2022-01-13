from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.RestrictedDiet import RestrictedDiet


class KosherDiet(RestrictedDiet):
    """A diet conforming to Jewish dietary practices.

    See: https://schema.org/KosherDiet
    Model depth: 5
    """

    type_: str = Field("KosherDiet", const=True, alias="@type")


if TYPE_CHECKING:

    KosherDiet.update_forward_refs()
