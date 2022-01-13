from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty

from pydantic_schemaorg.MedicalBusiness import MedicalBusiness


class Gynecologic(MedicalSpecialty, MedicalBusiness):
    """A specific branch of medical science that pertains to the health care of women, particularly"
     "in the diagnosis and treatment of disorders affecting the female reproductive system.

    See: https://schema.org/Gynecologic
    Model depth: 5
    """

    type_: str = Field("Gynecologic", const=True, alias="@type")


if TYPE_CHECKING:

    Gynecologic.update_forward_refs()
