from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalDevicePurpose import MedicalDevicePurpose


class Diagnostic(MedicalDevicePurpose):
    """A medical device used for diagnostic purposes.

    See: https://schema.org/Diagnostic
    Model depth: 6
    """
    type_: str = Field("Diagnostic", alias='@type')
    

