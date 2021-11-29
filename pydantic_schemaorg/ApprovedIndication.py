from pydantic import Field
from pydantic_schemaorg.MedicalIndication import MedicalIndication


class ApprovedIndication(MedicalIndication):
    """An indication for a medical therapy that has been formally specified or approved by a"
     "regulatory body that regulates use of the therapy; for example, the US FDA approves indications"
     "for most drugs in the US.

    See https://schema.org/ApprovedIndication.

    """

    locals().update({"@type": Field("ApprovedIndication", const=True)})


ApprovedIndication.update_forward_refs()
