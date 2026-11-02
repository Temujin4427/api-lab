import pytest

# The pizza never needs a tool that the customer excluded.
@pytest.mark.parametrize(
    "excluded",
    [
        [],
        ["Knife"],
        ["Scissors"],
        ["Knife", "Scissors"],
    ],
)
def test_excluded_tool_is_not_used(api, auth, excluded):
    body = {"excludedTools": excluded}
    res = api.post("/api/pizza", json=body, headers=auth)
    assert res.status_code == 200
    assert res.json()["pizza"]["tool"] not in excluded

# Defect: Excluding all 3 tools makes QuickPizza return 500 instead of 400.
@pytest.mark.xfail(
    reason="Defect 1: Excluding all 3 tools causes 500 Internal Server Error instead of 400 Bad Request",
    strict=True,
    raises=AssertionError
)
def test_all_tools_excluded_is_refused(api, auth):
    all_tools = ["Knife", "Pizza cutter", "Scissors"]
    res = api.post("/api/pizza", json={"excludedTools": all_tools}, headers=auth)
    assert res.status_code == 400
    assert "error" in res.json()