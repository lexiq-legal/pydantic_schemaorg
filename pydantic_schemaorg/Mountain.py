from pydantic import Field
from pydantic_schemaorg.Landform import Landform


class Mountain(Landform):
    """A mountain, like Mount Whitney or Mount Everest.

    See https://schema.org/Mountain.

    """

    locals().update({"@type": Field("Mountain", const=True)})


Mountain.update_forward_refs()
