from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class ResultsNotAvailable(MedicalStudyStatus):
    """Results are not available.

    See: https://schema.org/ResultsNotAvailable
    Model depth: 6
    """

    type_: str = Field("ResultsNotAvailable", const=True, alias="@type")


if TYPE_CHECKING:

    ResultsNotAvailable.update_forward_refs()
