from pydantic import Field
from pydantic_schemaorg.MediaObject import MediaObject
from typing import Any, Union, List, Optional
from pydantic_schemaorg.HyperTocEntry import HyperTocEntry
from pydantic_schemaorg.CreativeWork import CreativeWork


class HyperToc(CreativeWork):
    """A HyperToc represents a hypertext table of contents for complex media objects, such"
     "as [[VideoObject]], [[AudioObject]]. Items in the table of contents are indicated"
     "using the [[tocEntry]] property, and typed [[HyperTocEntry]]. For cases where the"
     "same larger work is split into multiple files, [[associatedMedia]] can be used on individual"
     "[[HyperTocEntry]] items.

    See https://schema.org/HyperToc.

    """

    associatedMedia: Optional[Union[List[MediaObject], MediaObject]] = Field(
        None,
        description="A media object that encodes this CreativeWork. This property is a synonym for encoding.",
    )
    tocEntry: Optional[Union[List[HyperTocEntry], HyperTocEntry]] = Field(
        None,
        description="Indicates a [[HyperTocEntry]] in a [[HyperToc]].",
    )
    locals().update({"@type": Field("HyperToc", const=True)})


HyperToc.update_forward_refs()
