from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalEntity import MedicalEntity


class MedicalIndication(MedicalEntity):
    """A condition or factor that indicates use of a medical therapy, including signs, symptoms,"
     "risk factors, anatomical states, etc.

    See: https://schema.org/MedicalIndication
    Model depth: 3
    """

    type_: str = Field("MedicalIndication", const=True, alias="@type")


if TYPE_CHECKING:

    MedicalIndication.update_forward_refs()
