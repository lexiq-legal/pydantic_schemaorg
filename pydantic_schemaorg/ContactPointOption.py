from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Enumeration import Enumeration


class ContactPointOption(Enumeration):
    """Enumerated options related to a ContactPoint.

    See: https://schema.org/ContactPointOption
    Model depth: 4
    """

    type_: str = Field("ContactPointOption", const=True, alias="@type")


if TYPE_CHECKING:

    ContactPointOption.update_forward_refs()
