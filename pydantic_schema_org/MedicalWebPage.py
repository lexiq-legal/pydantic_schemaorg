from pydantic import Field
from pydantic_schema_org.MedicalAudienceType import MedicalAudienceType
from typing import Any, Optional, Union, List
from pydantic_schema_org.WebPage import WebPage


class MedicalWebPage(WebPage):
    """A web page that provides medical information.

    See https://schema.org/MedicalWebPage.

    """

    medicalAudience: Union[List[Union[MedicalAudienceType, Any]], Union[MedicalAudienceType, Any]] = Field(
        None,
        description="Medical audience for page.",
    )
    aspect: Optional[Union[List[str], str]] = Field(
        None,
        description="An aspect of medical practice that is considered on the page, such as 'diagnosis', 'treatment',"
     "'causes', 'prognosis', 'etiology', 'epidemiology', etc.",
    )
    locals().update({"@type": Field("MedicalWebPage", const=True)})


MedicalWebPage.update_forward_refs()
