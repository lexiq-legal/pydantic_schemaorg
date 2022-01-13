from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.LegalService import LegalService


class Notary(LegalService):
    """A notary.

    See: https://schema.org/Notary
    Model depth: 5
    """

    type_: str = Field("Notary", const=True, alias="@type")


if TYPE_CHECKING:

    Notary.update_forward_refs()
