from __future__ import annotations
from pydantic import Field
from typing import TYPE_CHECKING
from typing import Optional,List,Any,Union


class {{ model.valid_name }}({{model.parents | join(', ')}}):
    """{{ model.description | replace('\\n','\n') | format_description}}

    See: https://schema.org/{{ model.name }}
    Model depth: {{model.depth}}
    """
    type_: str = Field("{{ model.name }}", const=True, alias='@type')
    {% for field in model.fields -%}
    {{ field.valid_name }}: "{{ field.type }}" = Field(
        None,
        {%- if field.valid_name != field.name -%} alias="{{ field.name }}",{% endif %}
        description="{{ field.description | replace('\\n','\n') | format_description }}",
    )
    {% endfor %}


{% if model.field_imports %}
if TYPE_CHECKING:
{%- for import_ in model.field_imports %}
    from {{import_.classPath}} import {{import_.classes_ | join(', ')}}
{%- endfor %}
{% endif %}

#{{ model.valid_name }}.update_forward_refs({% for import_ in model.forward_refs -%}{% for class_ in import_.classes_ -%}{{class_}}={{class_}},{%- endfor %}{%- endfor %})