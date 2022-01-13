from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class ResultsAvailable(MedicalStudyStatus):
    """Results are available.

    See: https://schema.org/ResultsAvailable
    Model depth: 6
    """

    type_: str = Field("ResultsAvailable", const=True, alias="@type")


if TYPE_CHECKING:

    ResultsAvailable.update_forward_refs()
