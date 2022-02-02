{%- raw %}
types={
{%- endraw %}
{%- for k,v in pydantic_classes.items() %}
'{{v.valid_name}}': ('{{v.valid_name}}', 'pydantic_schemaorg.{{v.valid_name}}', '{{v.valid_name}}'),
{%- endfor %}
{%- raw %}
}
{%- endraw %}