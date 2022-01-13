from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.AggregateRating import AggregateRating


class EmployerAggregateRating(AggregateRating):
    """An aggregate rating of an Organization related to its role as an employer.

    See: https://schema.org/EmployerAggregateRating
    Model depth: 5
    """

    type_: str = Field("EmployerAggregateRating", const=True, alias="@type")


if TYPE_CHECKING:

    EmployerAggregateRating.update_forward_refs()
