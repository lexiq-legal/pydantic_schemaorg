from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Eye(PhysicalExam):
    """Eye or ophtalmological function assessment with clinical examination.

    See: https://schema.org/Eye
    Model depth: 5
    """

    type_: str = Field("Eye", const=True, alias="@type")


if TYPE_CHECKING:

    Eye.update_forward_refs()
