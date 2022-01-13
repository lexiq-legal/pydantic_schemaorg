from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration


class DrugCostCategory(MedicalEnumeration):
    """Enumerated categories of medical drug costs.

    See: https://schema.org/DrugCostCategory
    Model depth: 5
    """

    type_: str = Field("DrugCostCategory", const=True, alias="@type")


if TYPE_CHECKING:

    DrugCostCategory.update_forward_refs()
