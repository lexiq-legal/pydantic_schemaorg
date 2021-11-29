from pydantic import Field
from pydantic_schemaorg.Quantity import Quantity


class Duration(Quantity):
    """Quantity: Duration (use [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601)).

    See https://schema.org/Duration.

    """

    locals().update({"@type": Field("Duration", const=True)})


Duration.update_forward_refs()
