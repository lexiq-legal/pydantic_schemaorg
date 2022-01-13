from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Nose(PhysicalExam):
    """Nose function assessment with clinical examination.

    See: https://schema.org/Nose
    Model depth: 5
    """

    type_: str = Field("Nose", const=True, alias="@type")


if TYPE_CHECKING:

    Nose.update_forward_refs()
