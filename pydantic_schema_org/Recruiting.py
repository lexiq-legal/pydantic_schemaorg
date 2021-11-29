from pydantic import Field
from pydantic_schema_org.MedicalStudyStatus import MedicalStudyStatus


class Recruiting(MedicalStudyStatus):
    """Recruiting participants.

    See https://schema.org/Recruiting.

    """

    locals().update({"@type": Field("Recruiting", const=True)})


Recruiting.update_forward_refs()
