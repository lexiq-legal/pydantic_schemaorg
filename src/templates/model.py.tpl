{% for key, value in model.imports.items() -%}
from {{key}} import {{value | join(', ')}}
{% endfor %}

class {{ model.valid_name }}({{model.parents | join(', ')}}):
    """{{ model.description | replace('\\n','\n') | format_description}}

    See https://schema.org/{{ model.name }}.

    """

    {% for field in model.fields -%}
    {{ field.valid_name }}: {{ field.type }} = Field(
        None,
        {%- if field.valid_name != field.name -%} alias="{{ field.name }}",{% endif %}
        description="{{ field.description | format_description }}",
    )
    {% endfor -%}

    locals().update({"@type": Field("{{ model.name }}", const=True)})


{{ model.valid_name }}.update_forward_refs()
