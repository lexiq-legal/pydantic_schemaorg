from pydantic import Field
from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class Completed(MedicalStudyStatus):
    """Completed.

    See https://schema.org/Completed.

    """

    locals().update({"@type": Field("Completed", const=True)})


Completed.update_forward_refs()
