from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class Library(LocalBusiness):
    """A library.

    See https://schema.org/Library.

    """

    locals().update({"@type": Field("Library", const=True)})


Library.update_forward_refs()
