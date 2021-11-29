from pydantic import Field
from pydantic_schema_org.PeopleAudience import PeopleAudience
from pydantic_schema_org.Audience import Audience


class MedicalAudience(PeopleAudience, Audience):
    """Target audiences for medical web pages.

    See https://schema.org/MedicalAudience.

    """

    locals().update({"@type": Field("MedicalAudience", const=True)})


MedicalAudience.update_forward_refs()
