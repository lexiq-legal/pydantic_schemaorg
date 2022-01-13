from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Thing import Thing


class Intangible(Thing):
    """A utility class that serves as the umbrella for a number of 'intangible' things such as"
     "quantities, structured values, etc.

    See: https://schema.org/Intangible
    Model depth: 2
    """

    type_: str = Field("Intangible", const=True, alias="@type")


if TYPE_CHECKING:

    Intangible.update_forward_refs()
