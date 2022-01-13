from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.CivicStructure import CivicStructure


class TaxiStand(CivicStructure):
    """A taxi stand.

    See: https://schema.org/TaxiStand
    Model depth: 4
    """

    type_: str = Field("TaxiStand", const=True, alias="@type")


if TYPE_CHECKING:

    TaxiStand.update_forward_refs()
