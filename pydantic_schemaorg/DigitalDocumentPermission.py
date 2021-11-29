from pydantic import Field
from pydantic_schemaorg.DigitalDocumentPermissionType import DigitalDocumentPermissionType
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.Audience import Audience
from pydantic_schemaorg.ContactPoint import ContactPoint
from pydantic_schemaorg.Intangible import Intangible


class DigitalDocumentPermission(Intangible):
    """A permission for a particular person or group to access a particular file.

    See https://schema.org/DigitalDocumentPermission.

    """

    permissionType: Optional[Union[List[DigitalDocumentPermissionType], DigitalDocumentPermissionType]] = Field(
        None,
        description="The type of permission granted the person, organization, or audience.",
    )
    grantee: Optional[Union[List[Union[Organization, Person, Audience, ContactPoint]], Union[Organization, Person, Audience, ContactPoint]]] = Field(
        None,
        description="The person, organization, contact point, or audience that has been granted this permission.",
    )
    locals().update({"@type": Field("DigitalDocumentPermission", const=True)})


DigitalDocumentPermission.update_forward_refs()
