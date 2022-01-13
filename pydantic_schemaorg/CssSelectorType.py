from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Text import Text


class CssSelectorType(Text):
    """Text representing a CSS selector.

    See: https://schema.org/CssSelectorType
    Model depth: 6
    """

    type_: str = Field("CssSelectorType", const=True, alias="@type")


if TYPE_CHECKING:

    CssSelectorType.update_forward_refs()
