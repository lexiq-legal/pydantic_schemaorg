from __future__ import annotations
from typing import TYPE_CHECKING

{% for import_ in model.imports -%}
{% if import_.type == 'parent' %}
from {{import_.classPath}} import {{import_.classes_ | join(', ')}}
{% endif %}
{%- endfor %}

class {{ model.valid_name }}({{model.parents | join(', ')}}):
    """{{ model.description | replace('\\n','\n') | format_description}}

    See https://schema.org/{{ model.name }}.
    model depth: {{model.depth}}
    """
    type_: str = Field("{{ model.name }}", const=True, alias='@type')
