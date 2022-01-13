from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty

from pydantic_schemaorg.MedicalBusiness import MedicalBusiness


class PlasticSurgery(MedicalSpecialty, MedicalBusiness):
    """A specific branch of medical science that pertains to therapeutic or cosmetic repair"
     "or re-formation of missing, injured or malformed tissues or body parts by manual and"
     "instrumental means.

    See: https://schema.org/PlasticSurgery
    Model depth: 5
    """

    type_: str = Field("PlasticSurgery", const=True, alias="@type")


if TYPE_CHECKING:

    PlasticSurgery.update_forward_refs()
