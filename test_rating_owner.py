# Other user cannot read rating owned by another user.
def test_other_user_cannot_read_rating(api, auth, rating, other_auth):
    path = f"/api/ratings/{rating['id']}"
    res = api.get(path, headers=other_auth)
    assert 400 <= res.status_code < 500

    # Check owner can still read
    owner_res = api.get(path, headers=auth)
    assert owner_res.status_code == 200

# Other user cannot update rating owned by another user.
def test_other_user_cannot_update_rating(api, auth, rating, other_auth):
    path = f"/api/ratings/{rating['id']}"
    res = api.put(path, json={"stars": 5}, headers=other_auth)
    assert 400 <= res.status_code < 500

    # Check stars didn't change for owner
    owner_res = api.get(path, headers=auth)
    assert owner_res.json()["stars"] == rating["stars"]

# Other user cannot delete rating owned by another user.
def test_other_user_cannot_delete_rating(api, auth, rating, other_auth):
    path = f"/api/ratings/{rating['id']}"
    res = api.delete(path, headers=other_auth)
    assert 400 <= res.status_code < 500

    # Check rating still exists for owner
    owner_res = api.get(path, headers=auth)
    assert owner_res.status_code == 200