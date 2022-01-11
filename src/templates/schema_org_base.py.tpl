from pydantic import BaseModel


class SchemaOrgBase(BaseModel):
    #JSON-LD fields
    reverse_ = Field(alias='@reverse')
    id_ = Field(alias='@id')
    context_ = Field(alias='@context')
    graph_ = Field(alias='@graph')

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
