from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.RestrictedDiet import RestrictedDiet


class HinduDiet(RestrictedDiet):
    """A diet conforming to Hindu dietary practices, in particular, beef-free.

    See: https://schema.org/HinduDiet
    Model depth: 5
    """

    type_: str = Field("HinduDiet", const=True, alias="@type")


if TYPE_CHECKING:

    HinduDiet.update_forward_refs()
