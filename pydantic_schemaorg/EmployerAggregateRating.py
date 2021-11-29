from pydantic import Field
from pydantic_schemaorg.AggregateRating import AggregateRating


class EmployerAggregateRating(AggregateRating):
    """An aggregate rating of an Organization related to its role as an employer.

    See https://schema.org/EmployerAggregateRating.

    """

    locals().update({"@type": Field("EmployerAggregateRating", const=True)})


EmployerAggregateRating.update_forward_refs()
