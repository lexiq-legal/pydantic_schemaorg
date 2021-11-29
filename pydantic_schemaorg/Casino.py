from pydantic import Field
from pydantic_schemaorg.EntertainmentBusiness import EntertainmentBusiness


class Casino(EntertainmentBusiness):
    """A casino.

    See https://schema.org/Casino.

    """

    locals().update({"@type": Field("Casino", const=True)})


Casino.update_forward_refs()
