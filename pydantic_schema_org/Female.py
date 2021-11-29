from pydantic import Field
from pydantic_schema_org.GenderType import GenderType


class Female(GenderType):
    """The female gender.

    See https://schema.org/Female.

    """

    locals().update({"@type": Field("Female", const=True)})


Female.update_forward_refs()
