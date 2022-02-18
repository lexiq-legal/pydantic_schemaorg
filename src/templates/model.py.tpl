from __future__ import annotations
{%- if model.pydantic_imports %}
from typing import TYPE_CHECKING
{%- endif %}
{% if model.field_imports %}
{%- for import_ in model.field_imports %}
from {{import_.classPath}} import {{import_.classes_ | sort | join(', ')}}
{%- endfor %}
{% endif %}
{% for import_ in model.parent_imports%}
from {{import_.classPath}} import {{import_.classes_ | sort|join(', ')}}
{%- endfor %}


class {{ model.valid_name }}({{model.parents| sort(attribute='depth', reverse=True) | map(attribute='valid_name') | join(', ')}}):
    """{{ model.description | replace('\\n','\n') | format_description}}

    See: https://schema.org/{{ model.name }}
    Model depth: {{model.depth}}
    """
    type_: str = Field(default="{{ model.name }}", alias='@type', const=True)
    {% for field in model.fields -%}
    {{ field.valid_name }}: {{ field.type }} = Field(
        default=None,
        {%- if field.valid_name != field.name -%} alias="{{ field.name }}",{% endif %}
        description="{{ field.description | replace('\\n','\n') | format_description }}",
    )
    {% endfor %}
{% if model.pydantic_imports %}
if TYPE_CHECKING:
{%- for import_ in model.pydantic_imports %}
    from {{import_.classPath}} import {{import_.classes_ | join(', ')}}
{%- endfor %}
{% endif %}