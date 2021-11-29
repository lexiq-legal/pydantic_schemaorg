from pydantic import Field
from pydantic_schema_org.InfectiousAgentClass import InfectiousAgentClass


class Protozoa(InfectiousAgentClass):
    """Single-celled organism that causes an infection.

    See https://schema.org/Protozoa.

    """

    locals().update({"@type": Field("Protozoa", const=True)})


Protozoa.update_forward_refs()
