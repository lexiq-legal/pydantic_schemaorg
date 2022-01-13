from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty

from pydantic_schemaorg.MedicalBusiness import MedicalBusiness


class Pediatric(MedicalSpecialty, MedicalBusiness):
    """A specific branch of medical science that specializes in the care of infants, children"
     "and adolescents.

    See: https://schema.org/Pediatric
    Model depth: 5
    """

    type_: str = Field("Pediatric", const=True, alias="@type")


if TYPE_CHECKING:

    Pediatric.update_forward_refs()
