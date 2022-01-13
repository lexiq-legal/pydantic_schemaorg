from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class Withdrawn(MedicalStudyStatus):
    """Withdrawn.

    See: https://schema.org/Withdrawn
    Model depth: 6
    """

    type_: str = Field("Withdrawn", const=True, alias="@type")


if TYPE_CHECKING:

    Withdrawn.update_forward_refs()
