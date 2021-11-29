from pydantic import Field
from pydantic_schema_org.MedicalDevicePurpose import MedicalDevicePurpose


class Therapeutic(MedicalDevicePurpose):
    """A medical device used for therapeutic purposes.

    See https://schema.org/Therapeutic.

    """

    locals().update({"@type": Field("Therapeutic", const=True)})


Therapeutic.update_forward_refs()
