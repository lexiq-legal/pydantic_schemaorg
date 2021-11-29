from pydantic import Field
from pydantic_schema_org.CreativeWork import CreativeWork


class Manuscript(CreativeWork):
    """A book, document, or piece of music written by hand rather than typed or printed.

    See https://schema.org/Manuscript.

    """

    locals().update({"@type": Field("Manuscript", const=True)})


Manuscript.update_forward_refs()
