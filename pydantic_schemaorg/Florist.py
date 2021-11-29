from pydantic import Field
from pydantic_schemaorg.Store import Store


class Florist(Store):
    """A florist.

    See https://schema.org/Florist.

    """

    locals().update({"@type": Field("Florist", const=True)})


Florist.update_forward_refs()
