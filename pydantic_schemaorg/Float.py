from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Number import Number


class Float(Number):
    """Data type: Floating number.

    See: https://schema.org/Float
    Model depth: 6
    """

    type_: str = Field("Float", const=True, alias="@type")


if TYPE_CHECKING:

    Float.update_forward_refs()
