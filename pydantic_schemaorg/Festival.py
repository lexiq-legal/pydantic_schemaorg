from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Event import Event


class Festival(Event):
    """Event type: Festival.

    See: https://schema.org/Festival
    Model depth: 3
    """

    type_: str = Field("Festival", const=True, alias="@type")


if TYPE_CHECKING:

    Festival.update_forward_refs()
