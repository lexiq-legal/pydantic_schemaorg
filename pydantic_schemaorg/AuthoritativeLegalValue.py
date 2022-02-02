from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.LegalValueLevel import LegalValueLevel


class AuthoritativeLegalValue(LegalValueLevel):
    """Indicates that the publisher gives some special status to the publication of the document."
     "(\"The Queens Printer\" version of a UK Act of Parliament, or the PDF version of a Directive"
     "published by the EU Office of Publications). Something \"Authoritative\" is considered"
     "to be also [[OfficialLegalValue]]\".

    See: https://schema.org/AuthoritativeLegalValue
    Model depth: 5
    """
    type_: str = Field("AuthoritativeLegalValue", alias='@type')
    

