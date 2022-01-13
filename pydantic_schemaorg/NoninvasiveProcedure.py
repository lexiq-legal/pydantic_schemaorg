from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalProcedureType import MedicalProcedureType


class NoninvasiveProcedure(MedicalProcedureType):
    """A type of medical procedure that involves noninvasive techniques.

    See: https://schema.org/NoninvasiveProcedure
    Model depth: 6
    """

    type_: str = Field("NoninvasiveProcedure", const=True, alias="@type")


if TYPE_CHECKING:

    NoninvasiveProcedure.update_forward_refs()
