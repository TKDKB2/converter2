from pydantic import BaseModel


class RuleSchema(BaseModel):
    input: str
    output: str
    flags: list[str]


