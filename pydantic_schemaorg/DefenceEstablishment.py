from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.GovernmentBuilding import GovernmentBuilding


class DefenceEstablishment(GovernmentBuilding):
    """A defence establishment, such as an army or navy base.

    See: https://schema.org/DefenceEstablishment
    Model depth: 5
    """

    type_: str = Field("DefenceEstablishment", const=True, alias="@type")


if TYPE_CHECKING:

    DefenceEstablishment.update_forward_refs()
