from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.ContactPointOption import ContactPointOption


class TollFree(ContactPointOption):
    """The associated telephone number is toll free.

    See: https://schema.org/TollFree
    Model depth: 5
    """

    type_: str = Field("TollFree", const=True, alias="@type")


if TYPE_CHECKING:

    TollFree.update_forward_refs()
