import pytest

# Boundary values for updating a rating.
# Valid stars are 1 to 5. An invalid update must leave the rating unchanged.
@pytest.mark.parametrize("stars, expected_status", [
    (0, 400),
    (1, 200),
    (5, 200),
    (6, 400),
])
def test_update_rating_boundary_values(api, auth, rating, stars, expected_status):
    path = f"/api/ratings/{rating['id']}"
    res = api.put(path, json={"stars": stars}, headers=auth)
    assert res.status_code == expected_status

    # Always read the rating back to check if it changed correctly (or didn't change)
    read_res = api.get(path, headers=auth)
    assert read_res.status_code == 200
    
    if expected_status == 200:
        assert read_res.json()["stars"] == stars
    else:
        assert read_res.json()["stars"] == rating["stars"]