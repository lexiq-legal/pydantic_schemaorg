from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Code(CreativeWork):
    """Computer programming source code. Example: Full (compile ready) solutions, code snippet"
     "samples, scripts, templates.

    See https://schema.org/Code.

    """

    locals().update({"@type": Field("Code", const=True)})


Code.update_forward_refs()
