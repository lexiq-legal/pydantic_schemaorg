from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Surgical(MedicalSpecialty):
    """A specific branch of medical science that pertains to treating diseases, injuries and"
     "deformities by manual and instrumental means.

    See: https://schema.org/Surgical
    Model depth: 6
    """

    type_: str = Field("Surgical", const=True, alias="@type")


if TYPE_CHECKING:

    Surgical.update_forward_refs()
