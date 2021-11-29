from pydantic import Field
from pydantic_schemaorg.ComicStory import ComicStory
from pydantic_schemaorg.CoverArt import CoverArt


class ComicCoverArt(ComicStory, CoverArt):
    """The artwork on the cover of a comic.

    See https://schema.org/ComicCoverArt.

    """

    locals().update({"@type": Field("ComicCoverArt", const=True)})


ComicCoverArt.update_forward_refs()
