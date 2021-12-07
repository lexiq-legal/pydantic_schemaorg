from pydantic import Field
from pydantic_schemaorg.BookFormatType import BookFormatType


class GraphicNovel(BookFormatType):
    """Book format: GraphicNovel. May represent a bound collection of ComicIssue instances.

    See https://schema.org/GraphicNovel.

    """
    type_: str = Field("GraphicNovel", const=True, alias='@type')
    

GraphicNovel.update_forward_refs()
