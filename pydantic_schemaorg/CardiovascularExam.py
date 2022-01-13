from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.PhysicalExam import PhysicalExam


class CardiovascularExam(PhysicalExam):
    """Cardiovascular system assessment withclinical examination.

    See: https://schema.org/CardiovascularExam
    Model depth: 5
    """

    type_: str = Field("CardiovascularExam", const=True, alias="@type")


if TYPE_CHECKING:

    CardiovascularExam.update_forward_refs()
