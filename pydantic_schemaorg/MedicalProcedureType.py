from pydantic import Field
from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration


class MedicalProcedureType(MedicalEnumeration):
    """An enumeration that describes different types of medical procedures.

    See https://schema.org/MedicalProcedureType.

    """

    locals().update({"@type": Field("MedicalProcedureType", const=True)})


MedicalProcedureType.update_forward_refs()
