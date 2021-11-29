from pydantic import Field
from pydantic_schemaorg.MedicalTest import MedicalTest


class BloodTest(MedicalTest):
    """A medical test performed on a sample of a patient's blood.

    See https://schema.org/BloodTest.

    """

    locals().update({"@type": Field("BloodTest", const=True)})


BloodTest.update_forward_refs()
