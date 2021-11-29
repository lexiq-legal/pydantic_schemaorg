from pydantic import Field, StrictBool
from typing import Any, Union, List, Optional
from pydantic_schemaorg.MediaObject import MediaObject


class _3DModel(MediaObject):
    """A 3D model represents some kind of 3D content, which may have [[encoding]]s in one or more"
     "[[MediaObject]]s. Many 3D formats are available (e.g. see [Wikipedia](https://en.wikipedia.org/wiki/Category:3D_graphics_file_formats));"
     "specific encoding formats can be represented using the [[encodingFormat]] property"
     "applied to the relevant [[MediaObject]]. For the case of a single file published after"
     "Zip compression, the convention of appending '+zip' to the [[encodingFormat]] can"
     "be used. Geospatial, AR/VR, artistic/animation, gaming, engineering and scientific"
     "content can all be represented using [[3DModel]].

    See https://schema.org/3DModel.

    """

    isResizable: Optional[Union[List[StrictBool], StrictBool]] = Field(
        None,
        description="Whether the 3DModel allows resizing. For example, room layout applications often do"
     "not allow 3DModel elements to be resized to reflect reality.",
    )
    locals().update({"@type": Field("3DModel", const=True)})


_3DModel.update_forward_refs()
