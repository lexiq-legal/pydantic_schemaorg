from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Ear(PhysicalExam):
    """Ear function assessment with clinical examination.

    See: https://schema.org/Ear
    Model depth: 5
    """

    type_: str = Field("Ear", const=True, alias="@type")


if TYPE_CHECKING:

    Ear.update_forward_refs()
