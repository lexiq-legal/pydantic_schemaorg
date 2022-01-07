from pydantic import Field
from pydantic_schemaorg.PostalAddress import PostalAddress
from pydantic_schemaorg.Place import Place
from typing import List, Optional, Union
from pydantic_schemaorg.ArchiveOrganization import ArchiveOrganization
from pydantic_schemaorg.CreativeWork import CreativeWork


class ArchiveComponent(CreativeWork):
    """An intangible type to be applied to any archive content, carrying with it a set of properties"
     "required to describe archival items and collections.

    See https://schema.org/ArchiveComponent.

    """
    type_: str = Field("ArchiveComponent", const=True, alias='@type')
    itemLocation: Optional[Union[List[Union[str, PostalAddress, Place]], Union[str, PostalAddress, Place]]] = Field(
        None,
        description="Current location of the item.",
    )
    holdingArchive: Optional[Union[List[Union[ArchiveOrganization, str]], Union[ArchiveOrganization, str]]] = Field(
        None,
        description="[[ArchiveOrganization]] that holds, keeps or maintains the [[ArchiveComponent]].",
    )
    

ArchiveComponent.update_forward_refs()
