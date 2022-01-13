from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Infectious(MedicalSpecialty):
    """Something in medical science that pertains to infectious diseases i.e caused by bacterial,"
     "viral, fungal or parasitic infections.

    See: https://schema.org/Infectious
    Model depth: 6
    """

    type_: str = Field("Infectious", const=True, alias="@type")


if TYPE_CHECKING:

    Infectious.update_forward_refs()
