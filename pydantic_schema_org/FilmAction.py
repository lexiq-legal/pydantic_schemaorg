from pydantic import Field
from pydantic_schema_org.CreateAction import CreateAction


class FilmAction(CreateAction):
    """The act of capturing sound and moving images on film, video, or digitally.

    See https://schema.org/FilmAction.

    """

    locals().update({"@type": Field("FilmAction", const=True)})


FilmAction.update_forward_refs()
