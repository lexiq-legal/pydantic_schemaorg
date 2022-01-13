from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.LegalForceStatus import LegalForceStatus


class NotInForce(LegalForceStatus):
    """Indicates that a legislation is currently not in force.

    See: https://schema.org/NotInForce
    Model depth: 6
    """

    type_: str = Field("NotInForce", const=True, alias="@type")


if TYPE_CHECKING:

    NotInForce.update_forward_refs()
