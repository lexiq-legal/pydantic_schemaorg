from pydantic import Field
from pydantic_schemaorg.LegalValueLevel import LegalValueLevel


class UnofficialLegalValue(LegalValueLevel):
    """Indicates that a document has no particular or special standing (e.g. a republication"
     "of a law by a private publisher).

    See https://schema.org/UnofficialLegalValue.

    """

    locals().update({"@type": Field("UnofficialLegalValue", const=True)})


UnofficialLegalValue.update_forward_refs()
