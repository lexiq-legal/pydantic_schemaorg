from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.DrugPrescriptionStatus import DrugPrescriptionStatus


class OTC(DrugPrescriptionStatus):
    """The character of a medical substance, typically a medicine, of being available over"
     "the counter or not.

    See: https://schema.org/OTC
    Model depth: 6
    """

    type_: str = Field("OTC", const=True, alias="@type")


if TYPE_CHECKING:

    OTC.update_forward_refs()
