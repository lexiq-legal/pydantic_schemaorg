from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Lung(PhysicalExam):
    """Lung and respiratory system clinical examination.

    See: https://schema.org/Lung
    Model depth: 5
    """

    type_: str = Field("Lung", const=True, alias="@type")


if TYPE_CHECKING:

    Lung.update_forward_refs()
