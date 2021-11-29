from pydantic import Field
from pydantic_schema_org.LocalBusiness import LocalBusiness


class RadioStation(LocalBusiness):
    """A radio station.

    See https://schema.org/RadioStation.

    """

    locals().update({"@type": Field("RadioStation", const=True)})


RadioStation.update_forward_refs()
