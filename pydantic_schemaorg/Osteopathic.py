from pydantic import Field
from pydantic_schemaorg.MedicineSystem import MedicineSystem


class Osteopathic(MedicineSystem):
    """A system of medicine focused on promoting the body's innate ability to heal itself.

    See https://schema.org/Osteopathic.

    """

    locals().update({"@type": Field("Osteopathic", const=True)})


Osteopathic.update_forward_refs()
