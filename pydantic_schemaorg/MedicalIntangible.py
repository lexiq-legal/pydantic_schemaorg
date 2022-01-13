from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalEntity import MedicalEntity


class MedicalIntangible(MedicalEntity):
    """A utility class that serves as the umbrella for a number of 'intangible' things in the"
     "medical space.

    See: https://schema.org/MedicalIntangible
    Model depth: 3
    """

    type_: str = Field("MedicalIntangible", const=True, alias="@type")


if TYPE_CHECKING:

    MedicalIntangible.update_forward_refs()
