from pydantic import Field
from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class Suspended(MedicalStudyStatus):
    """Suspended.

    See https://schema.org/Suspended.

    """

    locals().update({"@type": Field("Suspended", const=True)})


Suspended.update_forward_refs()
