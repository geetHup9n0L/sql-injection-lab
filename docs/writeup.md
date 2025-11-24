# Writeup: SQLi Lab (compact)

## Vulnerability
- `/login` builds SQL by concatenating username/password into the query string.
- `/search` concatenates the `q` parameter into a LIKE clause: vulnerable to UNION-based injection.

## Exploit
- Use `/search?q=PAYLOAD` where PAYLOAD closes the LIKE string and appends a UNION SELECT.
- Because `products` SELECT has 3 columns (id, name, description) we use `UNION SELECT 1, group_concat(...), 3`.
- `group_concat` aggregates values so they can be returned in a single row/column.

Example payload to list tables:
`' UNION SELECT 1, group_concat(name, ';'), 3 FROM sqlite_master WHERE type='table' -- `

Example payload to dump users:
`' UNION SELECT 1, group_concat(username || ':' || password, ';'), 3 FROM users -- `

## Fix
- Use prepared statements / parameterized queries. See `patched_app.py` for the corrected code.
- Additional mitigations: least privilege DB user, input validation, WAF/rate-limiting.
