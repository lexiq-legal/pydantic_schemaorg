from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.GenderType import GenderType


class Female(GenderType):
    """The female gender.

    See: https://schema.org/Female
    Model depth: 5
    """

    type_: str = Field("Female", const=True, alias="@type")


if TYPE_CHECKING:

    Female.update_forward_refs()
