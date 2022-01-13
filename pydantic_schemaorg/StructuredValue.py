from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Intangible import Intangible


class StructuredValue(Intangible):
    """Structured values are used when the value of a property has a more complex structure than"
     "simply being a textual value or a reference to another thing.

    See: https://schema.org/StructuredValue
    Model depth: 3
    """

    type_: str = Field("StructuredValue", const=True, alias="@type")


if TYPE_CHECKING:

    StructuredValue.update_forward_refs()
