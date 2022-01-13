from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.AdministrativeArea import AdministrativeArea


class State(AdministrativeArea):
    """A state or province of a country.

    See: https://schema.org/State
    Model depth: 4
    """

    type_: str = Field("State", const=True, alias="@type")


if TYPE_CHECKING:

    State.update_forward_refs()
