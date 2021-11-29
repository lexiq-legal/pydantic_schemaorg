from pydantic import Field
from pydantic_schema_org.CoverArt import CoverArt
from pydantic_schema_org.ComicStory import ComicStory


class ComicCoverArt(CoverArt, ComicStory):
    """The artwork on the cover of a comic.

    See https://schema.org/ComicCoverArt.

    """

    locals().update({"@type": Field("ComicCoverArt", const=True)})


ComicCoverArt.update_forward_refs()
