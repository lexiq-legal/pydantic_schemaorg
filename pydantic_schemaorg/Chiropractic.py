from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicineSystem import MedicineSystem


class Chiropractic(MedicineSystem):
    """A system of medicine focused on the relationship between the body's structure, mainly"
     "the spine, and its functioning.

    See: https://schema.org/Chiropractic
    Model depth: 6
    """

    type_: str = Field("Chiropractic", const=True, alias="@type")


if TYPE_CHECKING:

    Chiropractic.update_forward_refs()
