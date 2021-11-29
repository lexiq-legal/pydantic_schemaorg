from pydantic import Field
from pydantic_schema_org.Organization import Organization


class Consortium(Organization):
    """A Consortium is a membership [[Organization]] whose members are typically Organizations.

    See https://schema.org/Consortium.

    """

    locals().update({"@type": Field("Consortium", const=True)})


Consortium.update_forward_refs()
