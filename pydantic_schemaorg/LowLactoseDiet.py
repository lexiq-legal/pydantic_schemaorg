from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.RestrictedDiet import RestrictedDiet


class LowLactoseDiet(RestrictedDiet):
    """A diet appropriate for people with lactose intolerance.

    See: https://schema.org/LowLactoseDiet
    Model depth: 5
    """

    type_: str = Field("LowLactoseDiet", const=True, alias="@type")


if TYPE_CHECKING:

    LowLactoseDiet.update_forward_refs()
