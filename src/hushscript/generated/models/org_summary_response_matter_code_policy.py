from typing import Literal

OrgSummaryResponseMatterCodePolicy = Literal["off", "optional", "required"]

ORG_SUMMARY_RESPONSE_MATTER_CODE_POLICY_VALUES: set[
    OrgSummaryResponseMatterCodePolicy
] = {
    "off",
    "optional",
    "required",
}


def check_org_summary_response_matter_code_policy(
    value: str,
) -> OrgSummaryResponseMatterCodePolicy:
    if value in ORG_SUMMARY_RESPONSE_MATTER_CODE_POLICY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ORG_SUMMARY_RESPONSE_MATTER_CODE_POLICY_VALUES!r}"
    )
