from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.CreativeWork import CreativeWork


class PublicationVolume(CreativeWork):
    """A part of a successively published publication such as a periodical or multi-volume"
     "work, often numbered. It may represent a time span, such as a year. See also [blog post](http://blog.schema.org/2014/09/schemaorg-support-for-bibliographic_2.html).

    See https://schema.org/PublicationVolume.

    """

    pageStart: Optional[Union[List[Union[int, str]], Union[int, str]]] = Field(
        None,
        description="The page on which the work starts; for example \"135\" or \"xiii\".",
    )
    volumeNumber: Optional[Union[List[Union[int, str]], Union[int, str]]] = Field(
        None,
        description="Identifies the volume of publication or multi-part work; for example, \"iii\" or \"2\".",
    )
    pagination: Optional[Union[List[str], str]] = Field(
        None,
        description="Any description of pages that is not separated into pageStart and pageEnd; for example,"
     "\"1-6, 9, 55\" or \"10-12, 46-49\".",
    )
    pageEnd: Optional[Union[List[Union[int, str]], Union[int, str]]] = Field(
        None,
        description="The page on which the work ends; for example \"138\" or \"xvi\".",
    )
    locals().update({"@type": Field("PublicationVolume", const=True)})


PublicationVolume.update_forward_refs()
