from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Store import Store


class Florist(Store):
    """A florist.

    See: https://schema.org/Florist
    Model depth: 5
    """

    type_: str = Field("Florist", const=True, alias="@type")


if TYPE_CHECKING:

    Florist.update_forward_refs()
