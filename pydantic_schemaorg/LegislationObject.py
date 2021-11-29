from pydantic import Field
from pydantic_schemaorg.LegalValueLevel import LegalValueLevel
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Legislation import Legislation
from pydantic_schemaorg.MediaObject import MediaObject


class LegislationObject(Legislation, MediaObject):
    """A specific object or file containing a Legislation. Note that the same Legislation can"
     "be published in multiple files. For example, a digitally signed PDF, a plain PDF and an"
     "HTML version.

    See https://schema.org/LegislationObject.

    """

    legislationLegalValue: Optional[Union[List[LegalValueLevel], LegalValueLevel]] = Field(
        None,
        description="The legal value of this legislation file. The same legislation can be written in multiple"
     "files with different legal values. Typically a digitally signed PDF have a \"stronger\""
     "legal value than the HTML file of the same act.",
    )
    locals().update({"@type": Field("LegislationObject", const=True)})


LegislationObject.update_forward_refs()
