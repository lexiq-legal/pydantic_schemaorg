from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalSign import MedicalSign


class VitalSign(MedicalSign):
    """Vital signs are measures of various physiological functions in order to assess the most"
     "basic body functions.

    See: https://schema.org/VitalSign
    Model depth: 6
    """

    type_: str = Field("VitalSign", const=True, alias="@type")


if TYPE_CHECKING:

    VitalSign.update_forward_refs()
