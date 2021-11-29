from pydantic import Field
from pydantic_schemaorg.MedicalProcedureType import MedicalProcedureType


class NoninvasiveProcedure(MedicalProcedureType):
    """A type of medical procedure that involves noninvasive techniques.

    See https://schema.org/NoninvasiveProcedure.

    """

    locals().update({"@type": Field("NoninvasiveProcedure", const=True)})


NoninvasiveProcedure.update_forward_refs()
