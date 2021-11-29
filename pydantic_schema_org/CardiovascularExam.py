from pydantic import Field
from pydantic_schema_org.PhysicalExam import PhysicalExam


class CardiovascularExam(PhysicalExam):
    """Cardiovascular system assessment withclinical examination.

    See https://schema.org/CardiovascularExam.

    """

    locals().update({"@type": Field("CardiovascularExam", const=True)})


CardiovascularExam.update_forward_refs()
