from pydantic import Field
from pydantic_schemaorg.LegalValueLevel import LegalValueLevel


class AuthoritativeLegalValue(LegalValueLevel):
    """Indicates that the publisher gives some special status to the publication of the document."
     "(\"The Queens Printer\" version of a UK Act of Parliament, or the PDF version of a Directive"
     "published by the EU Office of Publications). Something \"Authoritative\" is considered"
     "to be also [[OfficialLegalValue]]\".

    See https://schema.org/AuthoritativeLegalValue.

    """

    locals().update({"@type": Field("AuthoritativeLegalValue", const=True)})


AuthoritativeLegalValue.update_forward_refs()
