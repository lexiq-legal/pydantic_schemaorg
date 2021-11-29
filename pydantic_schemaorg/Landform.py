from pydantic import Field
from pydantic_schemaorg.Place import Place


class Landform(Place):
    """A landform or physical feature. Landform elements include mountains, plains, lakes,"
     "rivers, seascape and oceanic waterbody interface features such as bays, peninsulas,"
     "seas and so forth, including sub-aqueous terrain features such as submersed mountain"
     "ranges, volcanoes, and the great ocean basins.

    See https://schema.org/Landform.

    """

    locals().update({"@type": Field("Landform", const=True)})


Landform.update_forward_refs()
