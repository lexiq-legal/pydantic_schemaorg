from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class SpeechPathology(MedicalSpecialty):
    """The scientific study and treatment of defects, disorders, and malfunctions of speech"
     "and voice, as stuttering, lisping, or lalling, and of language disturbances, as aphasia"
     "or delayed language acquisition.

    See: https://schema.org/SpeechPathology
    Model depth: 6
    """

    type_: str = Field("SpeechPathology", const=True, alias="@type")


if TYPE_CHECKING:

    SpeechPathology.update_forward_refs()
