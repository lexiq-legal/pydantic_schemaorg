from pydantic import Field
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class CommunityHealth(MedicalBusiness, MedicalSpecialty):
    """A field of public health focusing on improving health characteristics of a defined population"
     "in relation with their geographical or environment areas.

    See https://schema.org/CommunityHealth.

    """

    locals().update({"@type": Field("CommunityHealth", const=True)})


CommunityHealth.update_forward_refs()
