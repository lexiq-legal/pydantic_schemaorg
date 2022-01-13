from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Pulmonary(MedicalSpecialty):
    """A specific branch of medical science that pertains to the study of the respiratory system"
     "and its respective disease states.

    See: https://schema.org/Pulmonary
    Model depth: 6
    """

    type_: str = Field("Pulmonary", const=True, alias="@type")


if TYPE_CHECKING:

    Pulmonary.update_forward_refs()
