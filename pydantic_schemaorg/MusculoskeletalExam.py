from pydantic import Field
from pydantic_schemaorg.PhysicalExam import PhysicalExam


class MusculoskeletalExam(PhysicalExam):
    """Musculoskeletal system clinical examination.

    See https://schema.org/MusculoskeletalExam.

    """
    type_: str = Field("MusculoskeletalExam", const=True, alias='@type')
    

MusculoskeletalExam.update_forward_refs()
