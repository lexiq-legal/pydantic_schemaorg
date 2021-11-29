from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class SheetMusic(CreativeWork):
    """Printed music, as opposed to performed or recorded music.

    See https://schema.org/SheetMusic.

    """

    locals().update({"@type": Field("SheetMusic", const=True)})


SheetMusic.update_forward_refs()
