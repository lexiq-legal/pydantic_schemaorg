from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.AggregateRating import AggregateRating


class EmployerAggregateRating(AggregateRating):
    """An aggregate rating of an Organization related to its role as an employer.

    See: https://schema.org/EmployerAggregateRating
    Model depth: 5
    """
    type_: str = Field("EmployerAggregateRating", alias='@type')
    

