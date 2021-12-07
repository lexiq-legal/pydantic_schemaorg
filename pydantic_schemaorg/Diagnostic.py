from pydantic import Field
from pydantic_schemaorg.MedicalDevicePurpose import MedicalDevicePurpose


class Diagnostic(MedicalDevicePurpose):
    """A medical device used for diagnostic purposes.

    See https://schema.org/Diagnostic.

    """
    type_: str = Field("Diagnostic", const=True, alias='@type')
    

Diagnostic.update_forward_refs()
