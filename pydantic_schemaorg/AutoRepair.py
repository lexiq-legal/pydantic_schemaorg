from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.AutomotiveBusiness import AutomotiveBusiness


class AutoRepair(AutomotiveBusiness):
    """Car repair business.

    See: https://schema.org/AutoRepair
    Model depth: 5
    """

    type_: str = Field("AutoRepair", const=True, alias="@type")


if TYPE_CHECKING:

    AutoRepair.update_forward_refs()
