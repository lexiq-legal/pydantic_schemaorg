from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.PhysicalExam import PhysicalExam


class MusculoskeletalExam(PhysicalExam):
    """Musculoskeletal system clinical examination.

    See: https://schema.org/MusculoskeletalExam
    Model depth: 5
    """

    type_: str = Field("MusculoskeletalExam", const=True, alias="@type")


if TYPE_CHECKING:

    MusculoskeletalExam.update_forward_refs()
