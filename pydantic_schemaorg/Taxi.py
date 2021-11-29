from pydantic import Field
from pydantic_schemaorg.Service import Service


class Taxi(Service):
    """A taxi.

    See https://schema.org/Taxi.

    """

    locals().update({"@type": Field("Taxi", const=True)})


Taxi.update_forward_refs()
