from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalBusiness import MedicalBusiness


class Optician(MedicalBusiness):
    """A store that sells reading glasses and similar devices for improving vision.

    See: https://schema.org/Optician
    Model depth: 5
    """

    type_: str = Field("Optician", const=True, alias="@type")


if TYPE_CHECKING:

    Optician.update_forward_refs()
