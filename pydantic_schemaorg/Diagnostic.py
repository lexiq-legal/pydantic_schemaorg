from pydantic import Field
from pydantic_schemaorg.MedicalDevicePurpose import MedicalDevicePurpose


class Diagnostic(MedicalDevicePurpose):
    """A medical device used for diagnostic purposes.

    See https://schema.org/Diagnostic.

    """

    locals().update({"@type": Field("Diagnostic", const=True)})


Diagnostic.update_forward_refs()
