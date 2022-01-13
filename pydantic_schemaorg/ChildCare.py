from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.LocalBusiness import LocalBusiness


class ChildCare(LocalBusiness):
    """A Childcare center.

    See: https://schema.org/ChildCare
    Model depth: 4
    """

    type_: str = Field("ChildCare", const=True, alias="@type")


if TYPE_CHECKING:

    ChildCare.update_forward_refs()
