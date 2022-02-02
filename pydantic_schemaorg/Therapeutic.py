from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalDevicePurpose import MedicalDevicePurpose


class Therapeutic(MedicalDevicePurpose):
    """A medical device used for therapeutic purposes.

    See: https://schema.org/Therapeutic
    Model depth: 6
    """
    type_: str = Field("Therapeutic", alias='@type')
    

