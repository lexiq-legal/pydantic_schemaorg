from pydantic import Field
from pydantic_schemaorg.Church import Church


class CatholicChurch(Church):
    """A Catholic church.

    See https://schema.org/CatholicChurch.

    """

    locals().update({"@type": Field("CatholicChurch", const=True)})


CatholicChurch.update_forward_refs()
