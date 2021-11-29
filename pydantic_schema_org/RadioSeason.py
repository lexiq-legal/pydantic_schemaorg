from pydantic import Field
from pydantic_schema_org.CreativeWorkSeason import CreativeWorkSeason


class RadioSeason(CreativeWorkSeason):
    """Season dedicated to radio broadcast and associated online delivery.

    See https://schema.org/RadioSeason.

    """

    locals().update({"@type": Field("RadioSeason", const=True)})


RadioSeason.update_forward_refs()
