from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Skin(PhysicalExam):
    """Skin assessment with clinical examination.

    See: https://schema.org/Skin
    Model depth: 5
    """

    type_: str = Field("Skin", const=True, alias="@type")


if TYPE_CHECKING:

    Skin.update_forward_refs()
