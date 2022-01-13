from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class PharmacySpecialty(MedicalSpecialty):
    """The practice or art and science of preparing and dispensing drugs and medicines.

    See: https://schema.org/PharmacySpecialty
    Model depth: 6
    """

    type_: str = Field("PharmacySpecialty", const=True, alias="@type")


if TYPE_CHECKING:

    PharmacySpecialty.update_forward_refs()
