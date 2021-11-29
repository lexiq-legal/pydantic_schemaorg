from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Atlas(CreativeWork):
    """A collection or bound volume of maps, charts, plates or tables, physical or in media form"
     "illustrating any subject.

    See https://schema.org/Atlas.

    """

    locals().update({"@type": Field("Atlas", const=True)})


Atlas.update_forward_refs()
