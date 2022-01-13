from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalProcedure import MedicalProcedure


class SurgicalProcedure(MedicalProcedure):
    """A medical procedure involving an incision with instruments; performed for diagnose,"
     "or therapeutic purposes.

    See: https://schema.org/SurgicalProcedure
    Model depth: 4
    """

    type_: str = Field("SurgicalProcedure", const=True, alias="@type")


if TYPE_CHECKING:

    SurgicalProcedure.update_forward_refs()
