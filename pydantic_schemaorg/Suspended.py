from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class Suspended(MedicalStudyStatus):
    """Suspended.

    See: https://schema.org/Suspended
    Model depth: 6
    """

    type_: str = Field("Suspended", const=True, alias="@type")


if TYPE_CHECKING:

    Suspended.update_forward_refs()
