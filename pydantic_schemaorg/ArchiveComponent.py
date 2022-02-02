from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class ArchiveComponent(CreativeWork):
    """An intangible type to be applied to any archive content, carrying with it a set of properties"
     "required to describe archival items and collections.

    See: https://schema.org/ArchiveComponent
    Model depth: 3
    """
    type_: str = Field("ArchiveComponent", alias='@type')
    itemLocation: Optional[Union[List[Union[str, 'Text', 'PostalAddress', 'Place']], str, 'Text', 'PostalAddress', 'Place']] = Field(
        None,
        description="Current location of the item.",
    )
    holdingArchive: Optional[Union[List[Union['ArchiveOrganization', str]], 'ArchiveOrganization', str]] = Field(
        None,
        description="[[ArchiveOrganization]] that holds, keeps or maintains the [[ArchiveComponent]].",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.PostalAddress import PostalAddress
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.ArchiveOrganization import ArchiveOrganization
