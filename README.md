# Simple Django example

Admin credentials:

- user: admin
- pass: admin012

API user credentials:

- user: api_new
- pass: admin012

```
curl http://127.0.0.1:8000/api/new \
 -X POST \
 -H "Content-Type: application/json" \
 -H "X-CSRFToken: db05Iw8QnloBgv84LnhwTom5NTbFtJnb" \
 -H "Cookie: csrftoken=db05Iw8QnloBgv84LnhwTom5NTbFtJnb" \
 -d '{"user":"api_new","pass":"admin012","title":"Title_001","body":"Body_001","pub_date":"2016-01-01"}'
```
