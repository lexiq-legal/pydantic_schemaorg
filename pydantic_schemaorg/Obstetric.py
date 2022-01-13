from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty

from pydantic_schemaorg.MedicalBusiness import MedicalBusiness


class Obstetric(MedicalSpecialty, MedicalBusiness):
    """A specific branch of medical science that specializes in the care of women during the"
     "prenatal and postnatal care and with the delivery of the child.

    See: https://schema.org/Obstetric
    Model depth: 5
    """

    type_: str = Field("Obstetric", const=True, alias="@type")


if TYPE_CHECKING:

    Obstetric.update_forward_refs()
