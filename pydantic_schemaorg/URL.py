from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Text import Text


class URL(Text):
    """Data type: URL.

    See: https://schema.org/URL
    Model depth: 6
    """

    type_: str = Field("URL", const=True, alias="@type")


if TYPE_CHECKING:

    URL.update_forward_refs()
