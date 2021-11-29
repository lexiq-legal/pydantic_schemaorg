from pydantic import Field
from pydantic_schemaorg.PeopleAudience import PeopleAudience
from pydantic_schemaorg.Audience import Audience


class MedicalAudience(PeopleAudience, Audience):
    """Target audiences for medical web pages.

    See https://schema.org/MedicalAudience.

    """

    locals().update({"@type": Field("MedicalAudience", const=True)})


MedicalAudience.update_forward_refs()