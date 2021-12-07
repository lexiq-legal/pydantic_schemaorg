from pydantic import Field
from pydantic_schemaorg.MedicalDevicePurpose import MedicalDevicePurpose


class Therapeutic(MedicalDevicePurpose):
    """A medical device used for therapeutic purposes.

    See https://schema.org/Therapeutic.

    """
    type_: str = Field("Therapeutic", const=True, alias='@type')
    

Therapeutic.update_forward_refs()
