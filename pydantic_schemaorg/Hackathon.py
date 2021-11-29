from pydantic import Field
from pydantic_schemaorg.Event import Event


class Hackathon(Event):
    """A [hackathon](https://en.wikipedia.org/wiki/Hackathon) event.

    See https://schema.org/Hackathon.

    """

    locals().update({"@type": Field("Hackathon", const=True)})


Hackathon.update_forward_refs()
