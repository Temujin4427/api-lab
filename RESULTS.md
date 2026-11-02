# API lab results

## Part 0

- Step 0.1, the number of pizza names: 18
- Step 0.3, status code of the request without a token: 401
- Step 0.4, the name of your pizza: The Low Napoletana
- Step 0.12, results of the three runs without a session (optional): FAILED, FAILED, PASSED. Without a session cookie (AWSALB), requests were routed to different backend servers by the load balancer, resulting in 401 Unauthorized on the first two login attempts.
- Step 0.16, blocks of "how many of the three tools are excluded": 0 excluded, 1 excluded, 2 excluded, 3 excluded (all excluded)

## Defect report

1. Title: Server returns 500 Internal Server Error when all cutting tools are excluded
2. Request: POST https://quickpizza.grafana.com/api/pizza with header `Authorization: token <token of a logged-in user>` and body {"excludedTools": ["Knife", "Pizza cutter", "Scissors"]}
3. Expected result: Status 400 Bad Request with a JSON error message explaining that no pizza satisfies the request
4. Actual result: Status 500 Internal Server Error with an empty response body
5. Severity: Medium. Only an edge-case input triggers it, no data is lost and it is not a security problem, but a valid request makes the server fail.

## Part A

Step A4, status codes when the other user reads, changes and deletes: Read: 404, Change: 404, Delete: 400

## Part B

1.

- Two kinds of failure: (a) defects that appear only when real parts work together, for example the 500 error with an empty body when all tools are excluded; (b) deployment problems, for example the load balancer sending requests to different servers, so the login failed with 401 when I used no session.
- Reason for unit tests with stubs as well: they are fast, run offline, can force error cases that are hard to trigger on a real server, and do not load the shared server.

2.

- The public token's ratings belong to everyone, so another student could change them while my test runs. A new user per test keeps every test isolated and independent of order.
- For Project 2, each test creates its own data with a unique name (for example from `uuid`), a fixture deletes it afterwards, tests never touch the data of other groups, and passwords are read from environment variables.

3.

- A single session preserves cookies (such as `AWSALB`), ensuring sticky routing to the same backend server instance across all requests.
- In Step 0.12, the 3 runs were FAILED, FAILED and PASSED. The user was created (201), but without the cookie the login went to a server that had never seen that user (each server keeps its own users), so the login failed with 401.

4.

- The block with all 3 tools excluded (`["Knife", "Pizza cutter", "Scissors"]`) revealed the defect.
- A 500 tells the client that the server failed, so it cannot tell whether to fix its request or to retry, and the empty body gives no reason. A 400 tells it that its request was wrong and why.
- With `xfail(strict=True)` the suite stays green while the defect is known, and the run fails as soon as QuickPizza fixes it, which tells me to remove the mark. Deleting the test would lose the record of the defect and the check that it stays fixed.

5.

- Base choice coverage needs 9 tests: 1 base choice + (3-1) + (4-1) + (2-1) + (3-1) = 1 + 2 + 3 + 1 + 2 = 9.
- All combinations coverage needs 72 tests: 3 x 4 x 2 x 3 = 72.

6.

- Status codes received: Read: 404, Change: 404, Delete: 400.
- Expected codes: 403 Forbidden or 404 Not Found. Read and change match this, and 404 is not a defect because it hides whether the ID exists. Delete does not match: it returns 400 Bad Request with the body `{"error":"rating ID ... not found"}`. The message treats the rating as missing, so 404 would be the consistent code, and 400 should mean that the request itself is malformed. I count this as a minor defect (low severity), not a security defect, because the delete was refused, the owner's rating stayed unchanged, and the message does not reveal that the rating exists.

7.

- Running curl with `madeup.txt` returns HTTP 200 and a list of 50 ratings (ids 1 to 8 and 37470 to 37511), for example `{"id":1,"stars":5,"pizza_id":1}`, although this made-up token never created any rating.
- Yes, this is a defect (broken authentication). The server accepts a made-up 16-character token that it never issued (a short token is refused with 401, so it appears to check only the format) and returns data that this token never created. A stranger could read the ratings of other people, and on a real system could read private data or, if writes were allowed, change or delete data and impersonate users by guessing tokens.

8.

- API tests check status codes, headers, exact JSON payload structures, and boundary errors faster and more reliably.
- Web page tests check front-end UI rendering, CSS styles, animations, and visual user interactions that APIs cannot test.
