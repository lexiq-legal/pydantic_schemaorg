from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class EducationalOccupationalCredential(CreativeWork):
    """An educational or occupational credential. A diploma, academic degree, certification,"
     "qualification, badge, etc., that may be awarded to a person or other entity that meets"
     "the requirements defined by the credentialer.

    See: https://schema.org/EducationalOccupationalCredential
    Model depth: 3
    """
    type_: str = Field("EducationalOccupationalCredential", alias='@type')
    validFor: Optional[Union[List[Union['Duration', str]], 'Duration', str]] = Field(
        None,
        description="The duration of validity of a permit or similar thing.",
    )
    competencyRequired: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'DefinedTerm']], AnyUrl, 'URL', str, 'Text', 'DefinedTerm']] = Field(
        None,
        description="Knowledge, skill, ability or personal attribute that must be demonstrated by a person"
     "or other entity in order to do something such as earn an Educational Occupational Credential"
     "or understand a LearningResource.",
    )
    educationalLevel: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'DefinedTerm']], AnyUrl, 'URL', str, 'Text', 'DefinedTerm']] = Field(
        None,
        description="The level in terms of progression through an educational or training context. Examples"
     "of educational levels include 'beginner', 'intermediate' or 'advanced', and formal"
     "sets of level indicators.",
    )
    recognizedBy: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        None,
        description="An organization that acknowledges the validity, value or utility of a credential. Note:"
     "recognition may include a process of quality assurance or accreditation.",
    )
    validIn: Optional[Union[List[Union['AdministrativeArea', str]], 'AdministrativeArea', str]] = Field(
        None,
        description="The geographic area where a permit or similar thing is valid.",
    )
    credentialCategory: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'DefinedTerm']], AnyUrl, 'URL', str, 'Text', 'DefinedTerm']] = Field(
        None,
        description="The category or type of credential being described, for example \"degree”, “certificate”,"
     "“badge”, or more specific term.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Duration import Duration
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.DefinedTerm import DefinedTerm
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
