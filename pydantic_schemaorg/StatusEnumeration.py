from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Enumeration import Enumeration


class StatusEnumeration(Enumeration):
    """Lists or enumerations dealing with status types.

    See: https://schema.org/StatusEnumeration
    Model depth: 4
    """

    type_: str = Field("StatusEnumeration", const=True, alias="@type")


if TYPE_CHECKING:

    StatusEnumeration.update_forward_refs()
