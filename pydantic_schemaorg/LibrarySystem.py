from pydantic import Field
from pydantic_schemaorg.Organization import Organization


class LibrarySystem(Organization):
    """A [[LibrarySystem]] is a collaborative system amongst several libraries.

    See https://schema.org/LibrarySystem.

    """

    locals().update({"@type": Field("LibrarySystem", const=True)})


LibrarySystem.update_forward_refs()
