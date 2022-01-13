from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Number import Number


class Integer(Number):
    """Data type: Integer.

    See: https://schema.org/Integer
    Model depth: 6
    """

    type_: str = Field("Integer", const=True, alias="@type")


if TYPE_CHECKING:

    Integer.update_forward_refs()
