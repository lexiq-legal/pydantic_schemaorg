from pydantic import BaseModel, Field
from typing import Any


class SchemaOrgBase(BaseModel):
    # JSON-LD fields
    reverse_: Any = Field(alias="@reverse")
    id_: Any = Field(alias="@id")
    context_: Any = Field(alias="@context")
    graph_: Any = Field(alias="@graph")

    def dict(self, *args, **kwargs):
        defaults = {"exclude_none": True, "by_alias": True}
        return super().dict(*args, **dict(defaults, **kwargs))

    def json(self, *args, **kwargs):
        defaults = {"exclude_none": True, "by_alias": True}
        return super().json(*args, **dict(defaults, **kwargs))

    class Config:
        allow_population_by_field_name = True
