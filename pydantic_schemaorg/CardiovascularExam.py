from pydantic import Field
from pydantic_schemaorg.PhysicalExam import PhysicalExam


class CardiovascularExam(PhysicalExam):
    """Cardiovascular system assessment withclinical examination.

    See https://schema.org/CardiovascularExam.

    """

    locals().update({"@type": Field("CardiovascularExam", const=True)})


CardiovascularExam.update_forward_refs()
