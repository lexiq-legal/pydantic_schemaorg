from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.CreativeWork import CreativeWork


class ArchiveComponent(CreativeWork):
    """An intangible type to be applied to any archive content, carrying with it a set of properties"
     "required to describe archival items and collections.

    See: https://schema.org/ArchiveComponent
    Model depth: 3
    """

    type_: str = Field("ArchiveComponent", const=True, alias="@type")
    itemLocation: "Optional[Union[List[Union[str, Place, PostalAddress]], Union[str, Place, PostalAddress]]]" = Field(
        None,
        description="Current location of the item.",
    )
    holdingArchive: "Optional[Union[List[Union[ArchiveOrganization, str]], Union[ArchiveOrganization, str]]]" = Field(
        None,
        description="[[ArchiveOrganization]] that holds, keeps or maintains the [[ArchiveComponent]].",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.Place import Place

    from pydantic_schemaorg.PostalAddress import PostalAddress

    from pydantic_schemaorg.ArchiveOrganization import ArchiveOrganization

    ArchiveComponent.update_forward_refs()
