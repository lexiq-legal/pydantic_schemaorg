from pydantic import Field
from pydantic_schemaorg.ArchiveComponent import ArchiveComponent
from typing import Any, Union, List, Optional
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class ArchiveOrganization(LocalBusiness):
    """An organization with archival holdings. An organization which keeps and preserves"
     "archival material and typically makes it accessible to the public.

    See https://schema.org/ArchiveOrganization.

    """

    archiveHeld: Optional[Union[List[ArchiveComponent], ArchiveComponent]] = Field(
        None,
        description="Collection, [fonds](https://en.wikipedia.org/wiki/Fonds), or item held, kept"
     "or maintained by an [[ArchiveOrganization]].",
    )
    locals().update({"@type": Field("ArchiveOrganization", const=True)})


ArchiveOrganization.update_forward_refs()
