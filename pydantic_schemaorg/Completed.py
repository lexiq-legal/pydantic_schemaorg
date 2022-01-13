from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class Completed(MedicalStudyStatus):
    """Completed.

    See: https://schema.org/Completed
    Model depth: 6
    """

    type_: str = Field("Completed", const=True, alias="@type")


if TYPE_CHECKING:

    Completed.update_forward_refs()
