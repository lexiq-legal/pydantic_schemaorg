from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.CreativeWork import CreativeWork


class MathSolver(CreativeWork):
    """A math solver which is capable of solving a subset of mathematical problems.

    See https://schema.org/MathSolver.

    """

    mathExpression: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="A mathematical expression (e.g. 'x^2-3x=0') that may be solved for a specific variable,"
     "simplified, or transformed. This can take many formats, e.g. LaTeX, Ascii-Math, or"
     "math as you would write with a keyboard.",
    )
    locals().update({"@type": Field("MathSolver", const=True)})


MathSolver.update_forward_refs()
