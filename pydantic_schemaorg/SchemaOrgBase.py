from pydantic import BaseModel


class SchemaOrgBase(BaseModel):

    def dict(self, *args, **kwargs):
        defaults = {
            "exclude_none": True,
            "by_alias": True
        }
        return super().dict(*args, **dict(defaults, **kwargs))

    class Config:
        allow_population_by_field_name = True
