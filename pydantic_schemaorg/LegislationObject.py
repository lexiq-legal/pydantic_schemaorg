from pydantic import Field
from pydantic_schemaorg.LegalValueLevel import LegalValueLevel
from typing import List, Optional, Union
from pydantic_schemaorg.MediaObject import MediaObject
from pydantic_schemaorg.Legislation import Legislation


class LegislationObject(MediaObject, Legislation):
    """A specific object or file containing a Legislation. Note that the same Legislation can"
     "be published in multiple files. For example, a digitally signed PDF, a plain PDF and an"
     "HTML version.

    See https://schema.org/LegislationObject.

    """
    type_: str = Field("LegislationObject", const=True, alias='@type')
    legislationLegalValue: Optional[Union[List[Union[LegalValueLevel, str]], Union[LegalValueLevel, str]]] = Field(
        None,
        description="The legal value of this legislation file. The same legislation can be written in multiple"
     "files with different legal values. Typically a digitally signed PDF have a \"stronger\""
     "legal value than the HTML file of the same act.",
    )
    

LegislationObject.update_forward_refs()
