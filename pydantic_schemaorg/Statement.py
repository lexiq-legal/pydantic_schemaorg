from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Statement(CreativeWork):
    """A statement about something, for example a fun or interesting fact. If known, the main"
     "entity this statement is about, can be indicated using mainEntity. For more formal claims"
     "(e.g. in Fact Checking), consider using [[Claim]] instead. Use the [[text]] property"
     "to capture the text of the statement.

    See https://schema.org/Statement.

    """

    locals().update({"@type": Field("Statement", const=True)})


Statement.update_forward_refs()
