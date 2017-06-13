# CapioAI Python Challenge

**By:** Daksh Gupta

**Language:** Python 3.5

**Packages Required:** python-docx, requests, bottlepy

### Execution:

To execute the executable script simply use the following command after navigating to the program directory:

```Batchfile
python main.py <transcriptID> <APIKey>
```

To run the server simply use the following command after navigating to the program directory:

```Batchfile
python server.py <IP> <PORT_as_integer>
```

The server accepts **GET** requests with the request header having `apiKey` label and an associated string.

Thre requests are only accepted at the URL: `http://IP:PORT/transcript/<transcriptID>`