from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicineSystem import MedicineSystem


class Ayurvedic(MedicineSystem):
    """A system of medicine that originated in India over thousands of years and that focuses"
     "on integrating and balancing the body, mind, and spirit.

    See: https://schema.org/Ayurvedic
    Model depth: 6
    """

    type_: str = Field("Ayurvedic", const=True, alias="@type")


if TYPE_CHECKING:

    Ayurvedic.update_forward_refs()
