from pydantic import BaseModel, Field
from typing import Any, Optional
from pydantic.typing import update_model_forward_refs

class SchemaOrgBase(BaseModel):
    #JSON-LD fields
    reverse_ : Optional[Any] = Field(alias='@reverse')
    id_ : Optional[Any] = Field(alias='@id')
    context_ : Optional[Any] = Field(alias='@context')
    graph_ : Optional[Any] = Field(alias='@graph')

    def dict(self, *args, **kwargs):
        defaults = {
            "exclude_none": True,
            "by_alias": True
        }
        return super().dict(*args, **dict(defaults, **kwargs))

    def json(self, *args, **kwargs):
        defaults = {
            "exclude_none": True,
            "by_alias": True
        }
        return super().json(*args, **dict(defaults, **kwargs))

    class Config:
        allow_population_by_field_name = True

    @classmethod
    def update_forward_refs(cls, **localns: Any) -> None:
        """
        Try to update ForwardRefs on fields based on this Model, globalns and localns.
        """
        print(cls.__fields__.values())
        update_model_forward_refs(cls, cls.__fields__.values(), cls.__config__.json_encoders, localns)
