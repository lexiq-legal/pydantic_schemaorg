from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Toxicologic(MedicalSpecialty):
    """A specific branch of medical science that is concerned with poisons, their nature, effects"
     "and detection and involved in the treatment of poisoning.

    See: https://schema.org/Toxicologic
    Model depth: 6
    """

    type_: str = Field("Toxicologic", const=True, alias="@type")


if TYPE_CHECKING:

    Toxicologic.update_forward_refs()
