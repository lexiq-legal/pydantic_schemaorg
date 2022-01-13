from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.LegalForceStatus import LegalForceStatus


class InForce(LegalForceStatus):
    """Indicates that a legislation is in force.

    See: https://schema.org/InForce
    Model depth: 6
    """

    type_: str = Field("InForce", const=True, alias="@type")


if TYPE_CHECKING:

    InForce.update_forward_refs()
