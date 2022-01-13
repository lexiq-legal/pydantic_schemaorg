from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.GenderType import GenderType


class Male(GenderType):
    """The male gender.

    See: https://schema.org/Male
    Model depth: 5
    """

    type_: str = Field("Male", const=True, alias="@type")


if TYPE_CHECKING:

    Male.update_forward_refs()
