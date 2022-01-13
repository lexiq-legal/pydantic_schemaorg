from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalTherapy import MedicalTherapy


class RadiationTherapy(MedicalTherapy):
    """A process of care using radiation aimed at improving a health condition.

    See: https://schema.org/RadiationTherapy
    Model depth: 6
    """

    type_: str = Field("RadiationTherapy", const=True, alias="@type")


if TYPE_CHECKING:

    RadiationTherapy.update_forward_refs()
