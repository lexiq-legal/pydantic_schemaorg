from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration

from pydantic_schemaorg.MedicalProcedure import MedicalProcedure


class PhysicalExam(MedicalEnumeration, MedicalProcedure):
    """A type of physical examination of a patient performed by a physician.

    See: https://schema.org/PhysicalExam
    Model depth: 4
    """

    type_: str = Field("PhysicalExam", const=True, alias="@type")


if TYPE_CHECKING:

    PhysicalExam.update_forward_refs()
