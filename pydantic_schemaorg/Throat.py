from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Throat(PhysicalExam):
    """Throat assessment with clinical examination.

    See: https://schema.org/Throat
    Model depth: 5
    """

    type_: str = Field("Throat", const=True, alias="@type")


if TYPE_CHECKING:

    Throat.update_forward_refs()
