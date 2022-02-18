from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.WebPage import WebPage


class MedicalWebPage(WebPage):
    """A web page that provides medical information.

    See: https://schema.org/MedicalWebPage
    Model depth: 4
    """
    type_: str = Field(default="MedicalWebPage", alias='@type', const=True)
    medicalAudience: Optional[Union[List[Union['MedicalAudienceType', 'MedicalAudience', str]], 'MedicalAudienceType', 'MedicalAudience', str]] = Field(
        default=None,
        description="Medical audience for page.",
    )
    aspect: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="An aspect of medical practice that is considered on the page, such as 'diagnosis', 'treatment',"
     "'causes', 'prognosis', 'etiology', 'epidemiology', etc.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.MedicalAudienceType import MedicalAudienceType
    from pydantic_schemaorg.MedicalAudience import MedicalAudience
    from pydantic_schemaorg.Text import Text
