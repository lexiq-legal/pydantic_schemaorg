from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty

from pydantic_schemaorg.MedicalBusiness import MedicalBusiness


class PublicHealth(MedicalSpecialty, MedicalBusiness):
    """Branch of medicine that pertains to the health services to improve and protect community"
     "health, especially epidemiology, sanitation, immunization, and preventive medicine.

    See: https://schema.org/PublicHealth
    Model depth: 5
    """

    type_: str = Field("PublicHealth", const=True, alias="@type")


if TYPE_CHECKING:

    PublicHealth.update_forward_refs()
