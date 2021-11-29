from pydantic import Field
from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration
from pydantic_schemaorg.MedicalProcedure import MedicalProcedure


class PhysicalExam(MedicalEnumeration, MedicalProcedure):
    """A type of physical examination of a patient performed by a physician.

    See https://schema.org/PhysicalExam.

    """

    locals().update({"@type": Field("PhysicalExam", const=True)})


PhysicalExam.update_forward_refs()
