from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Dentistry(MedicalSpecialty):
    """A branch of medicine that is involved in the dental care.

    See: https://schema.org/Dentistry
    Model depth: 6
    """

    type_: str = Field("Dentistry", const=True, alias="@type")


if TYPE_CHECKING:

    Dentistry.update_forward_refs()
