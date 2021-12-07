from pydantic import Field
from pydantic_schemaorg.MedicalAudienceType import MedicalAudienceType


class MedicalResearcher(MedicalAudienceType):
    """Medical researchers.

    See https://schema.org/MedicalResearcher.

    """
    type_: str = Field("MedicalResearcher", const=True, alias='@type')
    

MedicalResearcher.update_forward_refs()
