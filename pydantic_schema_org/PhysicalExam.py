from pydantic import Field
from pydantic_schema_org.MedicalProcedure import MedicalProcedure
from pydantic_schema_org.MedicalEnumeration import MedicalEnumeration


class PhysicalExam(MedicalProcedure, MedicalEnumeration):
    """A type of physical examination of a patient performed by a physician.

    See https://schema.org/PhysicalExam.

    """

    locals().update({"@type": Field("PhysicalExam", const=True)})


PhysicalExam.update_forward_refs()
