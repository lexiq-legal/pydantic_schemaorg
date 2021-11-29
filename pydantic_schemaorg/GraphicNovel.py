from pydantic import Field
from pydantic_schemaorg.BookFormatType import BookFormatType


class GraphicNovel(BookFormatType):
    """Book format: GraphicNovel. May represent a bound collection of ComicIssue instances.

    See https://schema.org/GraphicNovel.

    """

    locals().update({"@type": Field("GraphicNovel", const=True)})


GraphicNovel.update_forward_refs()
