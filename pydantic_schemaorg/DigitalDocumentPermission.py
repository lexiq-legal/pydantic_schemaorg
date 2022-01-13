from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.Intangible import Intangible


class DigitalDocumentPermission(Intangible):
    """A permission for a particular person or group to access a particular file.

    See: https://schema.org/DigitalDocumentPermission
    Model depth: 3
    """

    type_: str = Field("DigitalDocumentPermission", const=True, alias="@type")
    permissionType: "Optional[Union[List[Union[DigitalDocumentPermissionType, str]], Union[DigitalDocumentPermissionType, str]]]" = Field(
        None,
        description="The type of permission granted the person, organization, or audience.",
    )
    grantee: "Optional[Union[List[Union[Audience, ContactPoint, Person, Organization, str]], Union[Audience, ContactPoint, Person, Organization, str]]]" = Field(
        None,
        description="The person, organization, contact point, or audience that has been granted this permission.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.DigitalDocumentPermissionType import (
        DigitalDocumentPermissionType,
    )

    from pydantic_schemaorg.Audience import Audience

    from pydantic_schemaorg.ContactPoint import ContactPoint

    from pydantic_schemaorg.Person import Person

    from pydantic_schemaorg.Organization import Organization

    DigitalDocumentPermission.update_forward_refs()
