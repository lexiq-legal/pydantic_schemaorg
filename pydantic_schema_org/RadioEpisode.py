from pydantic import Field
from pydantic_schema_org.Episode import Episode


class RadioEpisode(Episode):
    """A radio episode which can be part of a series or season.

    See https://schema.org/RadioEpisode.

    """

    locals().update({"@type": Field("RadioEpisode", const=True)})


RadioEpisode.update_forward_refs()
