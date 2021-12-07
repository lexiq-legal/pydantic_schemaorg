from pydantic import Field
from pydantic_schemaorg.LegalValueLevel import LegalValueLevel


class DefinitiveLegalValue(LegalValueLevel):
    """Indicates a document for which the text is conclusively what the law says and is legally"
     "binding. (e.g. The digitally signed version of an Official Journal.) Something \"Definitive\""
     "is considered to be also [[AuthoritativeLegalValue]].

    See https://schema.org/DefinitiveLegalValue.

    """
    type_: str = Field("DefinitiveLegalValue", const=True, alias='@type')
    

DefinitiveLegalValue.update_forward_refs()
