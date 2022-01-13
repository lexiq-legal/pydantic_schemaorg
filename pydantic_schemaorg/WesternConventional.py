from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicineSystem import MedicineSystem


class WesternConventional(MedicineSystem):
    """The conventional Western system of medicine, that aims to apply the best available evidence"
     "gained from the scientific method to clinical decision making. Also known as conventional"
     "or Western medicine.

    See: https://schema.org/WesternConventional
    Model depth: 6
    """

    type_: str = Field("WesternConventional", const=True, alias="@type")


if TYPE_CHECKING:

    WesternConventional.update_forward_refs()
