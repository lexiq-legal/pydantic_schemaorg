from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.ActionStatusType import ActionStatusType


class CompletedActionStatus(ActionStatusType):
    """An action that has already taken place.

    See: https://schema.org/CompletedActionStatus
    Model depth: 6
    """

    type_: str = Field("CompletedActionStatus", const=True, alias="@type")


if TYPE_CHECKING:

    CompletedActionStatus.update_forward_refs()
