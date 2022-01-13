from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Dermatologic(MedicalSpecialty):
    """Something relating to or practicing dermatology.

    See: https://schema.org/Dermatologic
    Model depth: 6
    """

    type_: str = Field("Dermatologic", const=True, alias="@type")


if TYPE_CHECKING:

    Dermatologic.update_forward_refs()
