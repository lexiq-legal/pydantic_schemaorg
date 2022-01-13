from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.QualitativeValue import QualitativeValue


class BedType(QualitativeValue):
    """A type of bed. This is used for indicating the bed or beds available in an accommodation.

    See: https://schema.org/BedType
    Model depth: 5
    """

    type_: str = Field("BedType", const=True, alias="@type")


if TYPE_CHECKING:

    BedType.update_forward_refs()
