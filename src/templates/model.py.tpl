from __future__ import annotations
{% for import_ in model.imports -%}
{% if import_.type == 'parent' %}
from {{import_.classPath}} import {{import_.classes_ | join(', ')}}
{% endif %}
{%- endfor %}

class {{ model.valid_name }}({{model.parents | join(', ')}}):
    """{{ model.description | replace('\\n','\n') | format_description}}

    See https://schema.org/{{ model.name }}.

    """
    type_: str = Field("{{ model.name }}", const=True, alias='@type')
    {% for field in model.fields -%}
    {{ field.valid_name }}: "{{ field.type }}" = Field(
        None,
        {%- if field.valid_name != field.name -%} alias="{{ field.name }}",{% endif %}
        description="{{ field.description | replace('\\n','\n') | format_description }}",
    )
    {% endfor %}


{% for import_ in model.imports -%}
    {% if import_.type == 'field' -%}
from {{import_.classPath}} import {{import_.classes_ | join(', ')}}
    {% endif %}
{% endfor %}
{{ model.valid_name }}.update_forward_refs()