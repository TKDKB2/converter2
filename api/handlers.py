from fastapi import APIRouter
from .schema import RuleSchema
from rules_model import Rules


router = APIRouter(prefix="/rules", tags=["rules"])


rules = Rules()

@router.post("/create_rule")
def create_rule(rule: RuleSchema):
    """ Creating the rule """
    details = {
        "output": rule.output,
        "flags": rule.flags,
    }
    return rules.create_rule(rule.input, details)


@router.post("/delete_rule/{input_format}")
def delete_rule(input_format: str):
    """ Deleting the rule """
    return rules.delete_rule(input_format)


@router.post("/update_rule")
def update_rule(rule: RuleSchema):
    """ Updating the rule """
    details = {
        "output": rule.output,
        "flags": rule.flags,
    }
    return rules.update_rule(rule.input, details)


@router.get("/get_rule/{input_format}")
def get_rule(input_format: str):
    """ Getting the rule """
    return rules.read_rule(input_format)


@router.get("/get_all_rules")
def get_all_rules():
    """ Getting all the rules """
    return rules.read_all_rules()
