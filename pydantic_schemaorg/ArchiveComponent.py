from pydantic import Field
from pydantic_schemaorg.Place import Place
from typing import Any, Union, List, Optional
from pydantic_schemaorg.CreativeWork import CreativeWork


class ArchiveComponent(CreativeWork):
    """An intangible type to be applied to any archive content, carrying with it a set of properties"
     "required to describe archival items and collections.

    See https://schema.org/ArchiveComponent.

    """

    itemLocation: Union[List[Union[str, Place, Any]], Union[str, Place, Any]] = Field(
        None,
        description="Current location of the item.",
    )
    holdingArchive: Any = Field(
        None,
        description="[[ArchiveOrganization]] that holds, keeps or maintains the [[ArchiveComponent]].",
    )
    locals().update({"@type": Field("ArchiveComponent", const=True)})


ArchiveComponent.update_forward_refs()
