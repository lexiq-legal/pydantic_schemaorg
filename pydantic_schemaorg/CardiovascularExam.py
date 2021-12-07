from pydantic import Field
from pydantic_schemaorg.PhysicalExam import PhysicalExam


class CardiovascularExam(PhysicalExam):
    """Cardiovascular system assessment withclinical examination.

    See https://schema.org/CardiovascularExam.

    """
    type_: str = Field("CardiovascularExam", const=True, alias='@type')
    

CardiovascularExam.update_forward_refs()
