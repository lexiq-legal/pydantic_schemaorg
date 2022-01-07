from pydantic import Field
from pydantic_schemaorg.DigitalDocumentPermission import DigitalDocumentPermission
from typing import List, Optional, Union
from pydantic_schemaorg.CreativeWork import CreativeWork


class DigitalDocument(CreativeWork):
    """An electronic file or document.

    See https://schema.org/DigitalDocument.

    """
    type_: str = Field("DigitalDocument", const=True, alias='@type')
    hasDigitalDocumentPermission: Optional[Union[List[Union[DigitalDocumentPermission, str]], Union[DigitalDocumentPermission, str]]] = Field(
        None,
        description="A permission related to the access to this document (e.g. permission to read or write"
     "an electronic document). For a public document, specify a grantee with an Audience with"
     "audienceType equal to \"public\".",
    )
    

DigitalDocument.update_forward_refs()
