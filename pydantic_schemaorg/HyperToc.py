from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.CreativeWork import CreativeWork


class HyperToc(CreativeWork):
    """A HyperToc represents a hypertext table of contents for complex media objects, such"
     "as [[VideoObject]], [[AudioObject]]. Items in the table of contents are indicated"
     "using the [[tocEntry]] property, and typed [[HyperTocEntry]]. For cases where the"
     "same larger work is split into multiple files, [[associatedMedia]] can be used on individual"
     "[[HyperTocEntry]] items.

    See: https://schema.org/HyperToc
    Model depth: 3
    """

    type_: str = Field("HyperToc", const=True, alias="@type")
    associatedMedia: "Optional[Union[List[Union[MediaObject, str]], Union[MediaObject, str]]]" = Field(
        None,
        description="A media object that encodes this CreativeWork. This property is a synonym for encoding.",
    )
    tocEntry: "Optional[Union[List[Union[HyperTocEntry, str]], Union[HyperTocEntry, str]]]" = Field(
        None,
        description="Indicates a [[HyperTocEntry]] in a [[HyperToc]].",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.MediaObject import MediaObject

    from pydantic_schemaorg.HyperTocEntry import HyperTocEntry

    HyperToc.update_forward_refs()
