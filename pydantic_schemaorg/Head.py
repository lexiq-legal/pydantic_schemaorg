from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Head(PhysicalExam):
    """Head assessment with clinical examination.

    See: https://schema.org/Head
    Model depth: 5
    """

    type_: str = Field("Head", const=True, alias="@type")


if TYPE_CHECKING:

    Head.update_forward_refs()
