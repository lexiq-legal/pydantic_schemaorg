from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalBusiness import MedicalBusiness

from pydantic_schemaorg.MedicalOrganization import MedicalOrganization


class Pharmacy(MedicalBusiness, MedicalOrganization):
    """A pharmacy or drugstore.

    See: https://schema.org/Pharmacy
    Model depth: 4
    """

    type_: str = Field("Pharmacy", const=True, alias="@type")


if TYPE_CHECKING:

    Pharmacy.update_forward_refs()
