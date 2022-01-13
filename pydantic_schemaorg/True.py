from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Boolean import Boolean


class True_(Boolean):
    """The boolean value true.

    See: https://schema.org/True
    Model depth: 6
    """

    type_: str = Field("True", const=True, alias="@type")


if TYPE_CHECKING:

    True_.update_forward_refs()
