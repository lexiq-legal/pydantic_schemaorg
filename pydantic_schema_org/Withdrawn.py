from pydantic import Field
from pydantic_schema_org.MedicalStudyStatus import MedicalStudyStatus


class Withdrawn(MedicalStudyStatus):
    """Withdrawn.

    See https://schema.org/Withdrawn.

    """

    locals().update({"@type": Field("Withdrawn", const=True)})


Withdrawn.update_forward_refs()
