from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalDevicePurpose import MedicalDevicePurpose


class Therapeutic(MedicalDevicePurpose):
    """A medical device used for therapeutic purposes.

    See: https://schema.org/Therapeutic
    Model depth: 6
    """

    type_: str = Field("Therapeutic", const=True, alias="@type")


if TYPE_CHECKING:

    Therapeutic.update_forward_refs()
