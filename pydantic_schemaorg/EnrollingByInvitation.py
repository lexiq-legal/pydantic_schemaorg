from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class EnrollingByInvitation(MedicalStudyStatus):
    """Enrolling participants by invitation only.

    See: https://schema.org/EnrollingByInvitation
    Model depth: 6
    """

    type_: str = Field("EnrollingByInvitation", const=True, alias="@type")


if TYPE_CHECKING:

    EnrollingByInvitation.update_forward_refs()
