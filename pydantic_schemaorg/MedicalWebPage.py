from pydantic import Field
from pydantic_schemaorg.MedicalAudienceType import MedicalAudienceType
from pydantic_schemaorg.MedicalAudience import MedicalAudience
from typing import List, Optional, Any, Union
from pydantic_schemaorg.WebPage import WebPage


class MedicalWebPage(WebPage):
    """A web page that provides medical information.

    See https://schema.org/MedicalWebPage.

    """
    type_: str = Field("MedicalWebPage", const=True, alias='@type')
    medicalAudience: Optional[Union[List[Union[MedicalAudienceType, MedicalAudience, str]], Union[MedicalAudienceType, MedicalAudience, str]]] = Field(
        None,
        description="Medical audience for page.",
    )
    aspect: Optional[Union[List[str], str]] = Field(
        None,
        description="An aspect of medical practice that is considered on the page, such as 'diagnosis', 'treatment',"
     "'causes', 'prognosis', 'etiology', 'epidemiology', etc.",
    )
    

MedicalWebPage.update_forward_refs()
