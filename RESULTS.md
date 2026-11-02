# API lab results

## Part 0

- Step 0.1, the number of pizza names: 18
- Step 0.3, status code of the request without a token: 401
- Step 0.4, the name of your pizza: The Low Napoletana
- Step 0.12, results of the three runs without a session (optional): FAILED, FAILED, PASSED เนื่องจากไม่มี Session Cookie (`AWSALB`) Load Balancer จึงสุ่มส่ง Request ไปยัง Backend Server คนละตัวกัน ทำให้ 2 ครั้งแรกโดนปฏิเสธด้วย 401 Unauthorized
- Step 0.16, blocks of "how many of the three tools are excluded": 0 excluded, 1 excluded, 2 excluded, 3 excluded (all excluded)

## Defect report

Title: Server returns 500 Internal Server Error when all cutting tools are excluded
Request: POST https://quickpizza.grafana.com/api/pizza with body {"excludedTools": ["Knife", "Pizza cutter", "Scissors"]}
Expected result: Status 400 Bad Request พร้อมข้อความ Error รูปแบบ JSON เพื่อแจ้งว่าไม่มีพิซซ่าที่ตรงกับเงื่อนไขนี้
Actual result: Status 500 Internal Server Error โดยไม่มี Response Body (Empty body)
Severity: High

## Part A

Step A4, status codes when the other user reads, changes and deletes: 404, Change: 404, Delete: 404

## Part B

1.

- Two kinds of failures: Network/connectivity issues between client and server, and server-side configuration/environment or Load Balancer routing failures.
- Reason for unit tests with stubs: Fast execution, isolation from external dependency failures, and ease of running offline in CI environments.

2.

- Creating a new user prevents test interference and state contamination when multiple test runs or users run tests concurrently.
- For Project 2, each test/suite should generate unique resource identifiers or isolated user sessions so operations do not conflict.

3.

- A single session preserves cookies (such as `AWSALB`), ensuring sticky routing to the same backend server instance across all requests.
- In Step 0.12, the 3 runs resulted in FAILED (401), FAILED (401), and PASSED because without session cookies, the load balancer routed requests to different backend instances that lacked the created user session.

4.

- The block with all 3 tools excluded (`["Knife", "Pizza cutter", "Scissors"]`) revealed the defect.
- A 500 error with an empty body implies an unhandled server crash, offering no context for the client, whereas a 400 error provides structured feedback.
- Marking it as `xfail` keeps the test suite green while tracking the known defect, and alerts us (via XPASS) as soon as the issue is resolved.

5.

- Base choice coverage needs 9 tests: 1 base choice + (3-1) + (4-1) + (2-1) + (3-1) = 1 + 2 + 3 + 1 + 2 = 9.
- All combinations coverage needs 72 tests: 3 _ 4 _ 2 \* 3 = 72.

6.

- Status codes received: Read: 404, Change: 404, Delete: 404.
- Expected codes: 403 Forbidden or 404 Not Found. Returning 404 is not a defect; it is standard security practice to prevent unauthorized users from discovering existing IDs.

7.

- Running curl with `madeup.txt` returns HTTP 200 with public ratings.
- This is a potential privacy/security risk as unauthenticated or arbitrary tokens can inspect system rating.

8.

- API tests check status codes, headers, exact JSON payload structures, and boundary errors faster and more reliably.
- Web page tests check front-end UI rendering, CSS styles, animations, and visual user interactions that APIs cannot test.
