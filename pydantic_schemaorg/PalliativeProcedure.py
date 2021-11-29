from pydantic import Field
from pydantic_schemaorg.MedicalTherapy import MedicalTherapy
from pydantic_schemaorg.MedicalProcedure import MedicalProcedure


class PalliativeProcedure(MedicalTherapy, MedicalProcedure):
    """A medical procedure intended primarily for palliative purposes, aimed at relieving"
     "the symptoms of an underlying health condition.

    See https://schema.org/PalliativeProcedure.

    """

    locals().update({"@type": Field("PalliativeProcedure", const=True)})


PalliativeProcedure.update_forward_refs()
