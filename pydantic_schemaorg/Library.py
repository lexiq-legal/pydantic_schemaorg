from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class Library(LocalBusiness):
    """A library.

    See https://schema.org/Library.

    """
    type_: str = Field("Library", const=True, alias='@type')
    

Library.update_forward_refs()
