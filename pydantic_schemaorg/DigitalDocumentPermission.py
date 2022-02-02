from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class DigitalDocumentPermission(Intangible):
    """A permission for a particular person or group to access a particular file.

    See: https://schema.org/DigitalDocumentPermission
    Model depth: 3
    """
    type_: str = Field("DigitalDocumentPermission", alias='@type')
    permissionType: Optional[Union[List[Union['DigitalDocumentPermissionType', str]], 'DigitalDocumentPermissionType', str]] = Field(
        None,
        description="The type of permission granted the person, organization, or audience.",
    )
    grantee: Optional[Union[List[Union['Person', 'Audience', 'Organization', 'ContactPoint', str]], 'Person', 'Audience', 'Organization', 'ContactPoint', str]] = Field(
        None,
        description="The person, organization, contact point, or audience that has been granted this permission.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.DigitalDocumentPermissionType import DigitalDocumentPermissionType
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Audience import Audience
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.ContactPoint import ContactPoint
