from pydantic import Field
from pydantic_schemaorg.LegalValueLevel import LegalValueLevel


class OfficialLegalValue(LegalValueLevel):
    """All the documents published by an official publisher should have at least the legal value"
     "level \"OfficialLegalValue\". This indicates that the document was published by an"
     "organisation with the public task of making it available (e.g. a consolidated version"
     "of a EU directive published by the EU Office of Publications).

    See https://schema.org/OfficialLegalValue.

    """

    locals().update({"@type": Field("OfficialLegalValue", const=True)})


OfficialLegalValue.update_forward_refs()
