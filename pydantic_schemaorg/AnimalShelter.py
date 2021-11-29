from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class AnimalShelter(LocalBusiness):
    """Animal shelter.

    See https://schema.org/AnimalShelter.

    """

    locals().update({"@type": Field("AnimalShelter", const=True)})


AnimalShelter.update_forward_refs()
