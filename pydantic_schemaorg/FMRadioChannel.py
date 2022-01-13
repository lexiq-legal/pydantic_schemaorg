from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.RadioChannel import RadioChannel


class FMRadioChannel(RadioChannel):
    """A radio channel that uses FM.

    See: https://schema.org/FMRadioChannel
    Model depth: 5
    """

    type_: str = Field("FMRadioChannel", const=True, alias="@type")


if TYPE_CHECKING:

    FMRadioChannel.update_forward_refs()
