from pydantic import Field
from pydantic_schemaorg.MedicineSystem import MedicineSystem


class Ayurvedic(MedicineSystem):
    """A system of medicine that originated in India over thousands of years and that focuses"
     "on integrating and balancing the body, mind, and spirit.

    See https://schema.org/Ayurvedic.

    """

    locals().update({"@type": Field("Ayurvedic", const=True)})


Ayurvedic.update_forward_refs()
