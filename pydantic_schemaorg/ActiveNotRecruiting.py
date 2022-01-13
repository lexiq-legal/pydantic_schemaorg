from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class ActiveNotRecruiting(MedicalStudyStatus):
    """Active, but not recruiting new participants.

    See: https://schema.org/ActiveNotRecruiting
    Model depth: 6
    """

    type_: str = Field("ActiveNotRecruiting", const=True, alias="@type")


if TYPE_CHECKING:

    ActiveNotRecruiting.update_forward_refs()
