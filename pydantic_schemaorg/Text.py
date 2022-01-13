from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.DataType import DataType


class Text(DataType):
    """Data type: Text.

    See: https://schema.org/Text
    Model depth: 5
    """

    type_: str = Field("Text", const=True, alias="@type")


if TYPE_CHECKING:

    Text.update_forward_refs()
