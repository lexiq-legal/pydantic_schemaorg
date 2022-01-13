from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class Recruiting(MedicalStudyStatus):
    """Recruiting participants.

    See: https://schema.org/Recruiting
    Model depth: 6
    """

    type_: str = Field("Recruiting", const=True, alias="@type")


if TYPE_CHECKING:

    Recruiting.update_forward_refs()
