from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalOrganization import MedicalOrganization


class VeterinaryCare(MedicalOrganization):
    """A vet's office.

    See: https://schema.org/VeterinaryCare
    Model depth: 4
    """

    type_: str = Field("VeterinaryCare", const=True, alias="@type")


if TYPE_CHECKING:

    VeterinaryCare.update_forward_refs()
