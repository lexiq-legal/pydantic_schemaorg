from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Quantity import Quantity


class Duration(Quantity):
    """Quantity: Duration (use [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601)).

    See: https://schema.org/Duration
    Model depth: 4
    """

    type_: str = Field("Duration", const=True, alias="@type")


if TYPE_CHECKING:

    Duration.update_forward_refs()
