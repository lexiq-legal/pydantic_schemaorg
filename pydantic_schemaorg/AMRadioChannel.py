from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.RadioChannel import RadioChannel


class AMRadioChannel(RadioChannel):
    """A radio channel that uses AM.

    See: https://schema.org/AMRadioChannel
    Model depth: 5
    """

    type_: str = Field("AMRadioChannel", const=True, alias="@type")


if TYPE_CHECKING:

    AMRadioChannel.update_forward_refs()
