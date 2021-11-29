from pydantic import Field
from pydantic_schema_org.Enumeration import Enumeration


class StatusEnumeration(Enumeration):
    """Lists or enumerations dealing with status types.

    See https://schema.org/StatusEnumeration.

    """

    locals().update({"@type": Field("StatusEnumeration", const=True)})


StatusEnumeration.update_forward_refs()
