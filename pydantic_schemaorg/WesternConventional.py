from pydantic import Field
from pydantic_schemaorg.MedicineSystem import MedicineSystem


class WesternConventional(MedicineSystem):
    """The conventional Western system of medicine, that aims to apply the best available evidence"
     "gained from the scientific method to clinical decision making. Also known as conventional"
     "or Western medicine.

    See https://schema.org/WesternConventional.

    """

    locals().update({"@type": Field("WesternConventional", const=True)})


WesternConventional.update_forward_refs()
