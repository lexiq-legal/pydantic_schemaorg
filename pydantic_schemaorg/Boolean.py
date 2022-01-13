from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.DataType import DataType


class Boolean(DataType):
    """Boolean: True or False.

    See: https://schema.org/Boolean
    Model depth: 5
    """

    type_: str = Field("Boolean", const=True, alias="@type")


if TYPE_CHECKING:

    Boolean.update_forward_refs()
