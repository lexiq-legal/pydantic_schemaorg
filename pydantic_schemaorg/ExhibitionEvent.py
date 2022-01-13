from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Event import Event


class ExhibitionEvent(Event):
    """Event type: Exhibition event, e.g. at a museum, library, archive, tradeshow, ...

    See: https://schema.org/ExhibitionEvent
    Model depth: 3
    """

    type_: str = Field("ExhibitionEvent", const=True, alias="@type")


if TYPE_CHECKING:

    ExhibitionEvent.update_forward_refs()
