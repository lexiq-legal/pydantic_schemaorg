from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Statement(CreativeWork):
    """A statement about something, for example a fun or interesting fact. If known, the main"
     "entity this statement is about, can be indicated using mainEntity. For more formal claims"
     "(e.g. in Fact Checking), consider using [[Claim]] instead. Use the [[text]] property"
     "to capture the text of the statement.

    See: https://schema.org/Statement
    Model depth: 3
    """
    type_: str = Field("Statement", alias='@type')
    

