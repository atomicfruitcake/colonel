import kore

# Handler called for /httpclient
async def server(req):
    # Create an httpclient.
    client = kore.httpclient("https://kore.io")

    # Do a simple GET request.
    print("firing off request")
    status, body = await client.get()
    print("status: %d, body: '%s'" % (status, body))

    # Reuse and perform another GET request, returning headers too this time.
    status, headers, body = await client.get(return_headers=True)
    print("status: %d, headers: '%s'" % (status, headers))

    # What happens if we post something?
    status, body = await client.post(body=b"hello world")
    print("status: %d, body: '%s'" % (status, body))

    # Add some custom headers to our requests.
    status, body = await client.get(
        headers={
            "x-my-header": "async-http"
        }
    )

    req.response(200, b'async done')
