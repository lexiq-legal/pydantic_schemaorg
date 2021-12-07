from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class RadioStation(LocalBusiness):
    """A radio station.

    See https://schema.org/RadioStation.

    """
    type_: str = Field("RadioStation", const=True, alias='@type')
    

RadioStation.update_forward_refs()
