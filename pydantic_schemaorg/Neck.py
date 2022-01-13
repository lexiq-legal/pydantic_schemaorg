from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Neck(PhysicalExam):
    """Neck assessment with clinical examination.

    See: https://schema.org/Neck
    Model depth: 5
    """

    type_: str = Field("Neck", const=True, alias="@type")


if TYPE_CHECKING:

    Neck.update_forward_refs()
