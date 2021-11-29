from pydantic import Field
from pydantic_schemaorg.MedicineSystem import MedicineSystem


class Homeopathic(MedicineSystem):
    """A system of medicine based on the principle that a disease can be cured by a substance that"
     "produces similar symptoms in healthy people.

    See https://schema.org/Homeopathic.

    """

    locals().update({"@type": Field("Homeopathic", const=True)})


Homeopathic.update_forward_refs()
