from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.WebPage import WebPage


class MedicalWebPage(WebPage):
    """A web page that provides medical information.

    See: https://schema.org/MedicalWebPage
    Model depth: 4
    """

    type_: str = Field("MedicalWebPage", const=True, alias="@type")
    medicalAudience: "Optional[Union[List[Union[MedicalAudience, MedicalAudienceType, str]], Union[MedicalAudience, MedicalAudienceType, str]]]" = Field(
        None,
        description="Medical audience for page.",
    )
    aspect: "Optional[Union[List[str], str]]" = Field(
        None,
        description="An aspect of medical practice that is considered on the page, such as 'diagnosis', 'treatment',"
        "'causes', 'prognosis', 'etiology', 'epidemiology', etc.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.MedicalAudience import MedicalAudience

    from pydantic_schemaorg.MedicalAudienceType import MedicalAudienceType

    MedicalWebPage.update_forward_refs()
