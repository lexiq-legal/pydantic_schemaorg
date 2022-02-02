from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic import StrictBool
from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.MediaObject import MediaObject


class _3DModel(MediaObject):
    """A 3D model represents some kind of 3D content, which may have [[encoding]]s in one or more"
     "[[MediaObject]]s. Many 3D formats are available (e.g. see [Wikipedia](https://en.wikipedia.org/wiki/Category:3D_graphics_file_formats));"
     "specific encoding formats can be represented using the [[encodingFormat]] property"
     "applied to the relevant [[MediaObject]]. For the case of a single file published after"
     "Zip compression, the convention of appending '+zip' to the [[encodingFormat]] can"
     "be used. Geospatial, AR/VR, artistic/animation, gaming, engineering and scientific"
     "content can all be represented using [[3DModel]].

    See: https://schema.org/3DModel
    Model depth: 4
    """
    type_: str = Field("3DModel", alias='@type')
    isResizable: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        None,
        description="Whether the 3DModel allows resizing. For example, room layout applications often do"
     "not allow 3DModel elements to be resized to reflect reality.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Boolean import Boolean
