from datetime import time
from decimal import Decimal
from typing import Any, Optional, ForwardRef, List, Union

from pydantic import BaseModel, Field, StrictBool, AnyUrl
from pydantic.typing import update_model_forward_refs

from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic_schemaorg.__types__ import types

updated_models=set()

class SchemaOrgBase(BaseModel):
    #JSON-LD fields
    reverse_ : Optional[Any] = Field(None,alias='@reverse')
    id_ : Optional[Any] = Field(None,alias='@id')
    context_ : Optional[Any] = Field(None,alias='@context')
    graph_ : Optional[Any] = Field(None,alias='@graph')

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
    def get_classes_for_forward_ref(cls, field: Any) -> List[tuple]:
        classes = []
        if type(field.type_) == ForwardRef:
            t = field.type_
            u = t.__forward_code__
            v = u.co_consts
            for w in v:
                pydanticschema_org_type = types[w]
                mod = __import__(pydanticschema_org_type[1], fromlist=[pydanticschema_org_type[0]])
                class_ = getattr(mod, pydanticschema_org_type[0])
                classes.append((w, class_))
        return classes

    @classmethod
    def get_local_ns(cls):
        global updated_models
        localns = {}
        for k, v in cls.__fields__.items():
            classes = cls.get_classes_for_forward_ref(v)
            for class_name, class_ in classes:
                localns.update({class_name: class_})
        return localns

    @classmethod
    def update_forward_refs(cls, **localns: Any) -> None:
        """
        Try to update ForwardRefs on fields based on this Model, globalns and localns.
        """
        locals = {'Optional': Optional, 'List': List, 'Union': Union, 'StrictBool': StrictBool, 'AnyUrl': AnyUrl,
                  'Decimal': Decimal, 'time': time,'ISO8601Date':ISO8601Date}
        for cls_ in cls.mro():
            if hasattr(cls_, 'get_local_ns'):
                locals.update(cls_.get_local_ns())
        update_model_forward_refs(cls, cls.__fields__.values(), cls.__config__.json_encoders, locals)

    @classmethod
    def _update_all_fields(cls):
        for cls_ in cls.mro():
            if hasattr(cls_, 'get_classes_for_forward_ref'):
                for k in cls_.__fields__.keys():
                    if k not in updated_models:
                        field = cls_.__fields__[k]
                        classes = cls_.get_classes_for_forward_ref(field)
                        for class_name, class_ in classes:
                            class_.update_forward_refs()

    def __init__(__pydantic_self__, **data: Any) -> None:
        __pydantic_self__.update_forward_refs()
        for k, v in data.items():
            if k in __pydantic_self__.__fields__.keys():
                if k not in updated_models:
                    field = __pydantic_self__.__fields__[k]
                    classes = __pydantic_self__.get_classes_for_forward_ref(field)
                    for class_name, class_ in classes:
                        class_.update_forward_refs()
        super().__init__(**data)
