from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class Terminated(MedicalStudyStatus):
    """Terminated.

    See: https://schema.org/Terminated
    Model depth: 6
    """

    type_: str = Field("Terminated", const=True, alias="@type")


if TYPE_CHECKING:

    Terminated.update_forward_refs()
