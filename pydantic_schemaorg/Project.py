from pydantic import Field
from pydantic_schemaorg.Organization import Organization


class Project(Organization):
    """An enterprise (potentially individual but typically collaborative), planned to achieve"
     "a particular aim. Use properties from [[Organization]], [[subOrganization]]/[[parentOrganization]]"
     "to indicate project sub-structures.

    See https://schema.org/Project.

    """

    locals().update({"@type": Field("Project", const=True)})


Project.update_forward_refs()
