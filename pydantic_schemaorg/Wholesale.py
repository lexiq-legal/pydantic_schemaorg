from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.DrugCostCategory import DrugCostCategory


class Wholesale(DrugCostCategory):
    """The drug's cost represents the wholesale acquisition cost of the drug.

    See: https://schema.org/Wholesale
    Model depth: 6
    """

    type_: str = Field("Wholesale", const=True, alias="@type")


if TYPE_CHECKING:

    Wholesale.update_forward_refs()
