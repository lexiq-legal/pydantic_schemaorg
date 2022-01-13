from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Neuro(PhysicalExam):
    """Neurological system clinical examination.

    See: https://schema.org/Neuro
    Model depth: 5
    """

    type_: str = Field("Neuro", const=True, alias="@type")


if TYPE_CHECKING:

    Neuro.update_forward_refs()
