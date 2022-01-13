from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.ContactPointOption import ContactPointOption


class HearingImpairedSupported(ContactPointOption):
    """Uses devices to support users with hearing impairments.

    See: https://schema.org/HearingImpairedSupported
    Model depth: 5
    """

    type_: str = Field("HearingImpairedSupported", const=True, alias="@type")


if TYPE_CHECKING:

    HearingImpairedSupported.update_forward_refs()
