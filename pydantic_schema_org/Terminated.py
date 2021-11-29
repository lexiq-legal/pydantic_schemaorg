from pydantic import Field
from pydantic_schema_org.MedicalStudyStatus import MedicalStudyStatus


class Terminated(MedicalStudyStatus):
    """Terminated.

    See https://schema.org/Terminated.

    """

    locals().update({"@type": Field("Terminated", const=True)})


Terminated.update_forward_refs()
