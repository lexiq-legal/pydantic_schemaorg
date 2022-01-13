from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Church import Church


class CatholicChurch(Church):
    """A Catholic church.

    See: https://schema.org/CatholicChurch
    Model depth: 6
    """

    type_: str = Field("CatholicChurch", const=True, alias="@type")


if TYPE_CHECKING:

    CatholicChurch.update_forward_refs()
