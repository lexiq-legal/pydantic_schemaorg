from pydantic import Field
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Emergency(MedicalBusiness, MedicalSpecialty):
    """A specific branch of medical science that deals with the evaluation and initial treatment"
     "of medical conditions caused by trauma or sudden illness.

    See https://schema.org/Emergency.

    """

    locals().update({"@type": Field("Emergency", const=True)})


Emergency.update_forward_refs()
