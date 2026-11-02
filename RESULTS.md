# API lab results

## Part 0

- Step 0.1, the number of pizza names: 18
- Step 0.3, status code of the request without a token: 401
- Step 0.4, the name of your pizza: The Low Napoletana
- Step 0.12, results of the three runs without a session (optional): FAILED, FAILED, PASSED. Without a session cookie (AWSALB), requests were routed to different backend servers by the load balancer, resulting in 401 Unauthorized on the first two login attempts.
- Step 0.16, blocks of "how many of the three tools are excluded": 0 excluded, 1 excluded, 2 excluded, 3 excluded (all excluded)

## Defect report

Title: Server returns 500 Internal Server Error when all cutting tools are excluded
Request: POST https://quickpizza.grafana.com/api/pizza with body {"excludedTools": ["Knife", "Pizza cutter", "Scissors"]}
Expected result: Status 400 Bad Request with a JSON error message explaining that no pizza satisfies the request
Actual result: Status 500 Internal Server Error with an empty response body
Severity: High

## Part A

Step A4, status codes when the other user reads, changes and deletes:

## Part B

1.
2.
3.
4.
5.
6.
7.
8.
