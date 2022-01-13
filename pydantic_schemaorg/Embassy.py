from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.GovernmentBuilding import GovernmentBuilding


class Embassy(GovernmentBuilding):
    """An embassy.

    See: https://schema.org/Embassy
    Model depth: 5
    """

    type_: str = Field("Embassy", const=True, alias="@type")


if TYPE_CHECKING:

    Embassy.update_forward_refs()
