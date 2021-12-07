from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Manuscript(CreativeWork):
    """A book, document, or piece of music written by hand rather than typed or printed.

    See https://schema.org/Manuscript.

    """
    type_: str = Field("Manuscript", const=True, alias='@type')
    

Manuscript.update_forward_refs()
