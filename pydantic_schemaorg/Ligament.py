from pydantic import Field
from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure


class Ligament(AnatomicalStructure):
    """A short band of tough, flexible, fibrous connective tissue that functions to connect"
     "multiple bones, cartilages, and structurally support joints.

    See https://schema.org/Ligament.

    """

    locals().update({"@type": Field("Ligament", const=True)})


Ligament.update_forward_refs()
