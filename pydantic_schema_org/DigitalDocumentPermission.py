from pydantic import Field
from pydantic_schema_org.DigitalDocumentPermissionType import DigitalDocumentPermissionType
from typing import Any, Optional, Union, List
from pydantic_schema_org.Person import Person
from pydantic_schema_org.ContactPoint import ContactPoint
from pydantic_schema_org.Audience import Audience
from pydantic_schema_org.Organization import Organization
from pydantic_schema_org.Intangible import Intangible


class DigitalDocumentPermission(Intangible):
    """A permission for a particular person or group to access a particular file.

    See https://schema.org/DigitalDocumentPermission.

    """

    permissionType: Optional[Union[List[DigitalDocumentPermissionType], DigitalDocumentPermissionType]] = Field(
        None,
        description="The type of permission granted the person, organization, or audience.",
    )
    grantee: Optional[Union[List[Union[Person, ContactPoint, Audience, Organization]], Union[Person, ContactPoint, Audience, Organization]]] = Field(
        None,
        description="The person, organization, contact point, or audience that has been granted this permission.",
    )
    locals().update({"@type": Field("DigitalDocumentPermission", const=True)})


DigitalDocumentPermission.update_forward_refs()
