from fastapi import APIRouter
from .schema import RuleSchema
from rules_model import Rules


router = APIRouter(prefix="/rules", tags=["rules"])


rules = Rules()

""" Creating the rule """
@router.post("/create_rule")
def create_rule(rule: RuleSchema):
    details = {
        "output": rule.output,
        "flags": rule.flags,
    }
    return rules.create_rule(rule.input, details)


""" Deleting the rule """
@router.post("/delete_rule/{input_format}")
def delete_rule(input_format: str):
    return rules.delete_rule(input_format)


""" Updating the rule """
@router.post("/update_rule")
def update_rule(rule: RuleSchema):
    details = {
        "output": rule.output,
        "flags": rule.flags,
    }
    return rules.update_rule(rule.input, details)


""" Getting the rule """
@router.get("/get_rule/{input_format}")
def get_rule(input_format: str):
    return rules.read_rule(input_format)


""" Getting all the rules """
@router.get("/get_all_rules")
def get_all_rules():
    return rules.read_all_rules()
