import re
# 언어별 패턴 정의
PATTERNS = {
    'rb': {
        "network": [
            re.compile(r'\b(Net::|HTTParty|Net|HTTP|FTP|SMTP|POP3|IMAP|Telnet|Socket|TCPSocket|UDPSocket|OpenSSL|URI|RestClient|Faraday|Excon|Typhoeus|HTTPClient|Mechanize|EventMachine|HttpRequest|Celluloid|Resolv|IPAddr)\b', re.IGNORECASE)
        ],
        "file": [
            re.compile(r'\b(File|Dir|IO|FileUtils|Tempfile|Pathname)\b', re.IGNORECASE)
        ],
        "process": [
            re.compile(r'\b(Process|Thread|Fiber|Open3|system|exec)\b', re.IGNORECASE)
        ]
    },
    'py': {
        "network": [
            re.compile(r'\b(requests|http\.client|http\.server|socket|urllib|httplib|asyncio|ftplib|smtplib|imaplib|poplib|xmlrpc|websocket|twisted|aiohttp|flask|bottle|django|tornado|fastapi)\b', re.IGNORECASE)
        ],
        "file": [
            re.compile(r'\b(os|open|shutil|pathlib|tempfile|glob|pickle|csv|json|xml|h5py|zipfile|tarfile|io|fileinput)\b', re.IGNORECASE)
        ],
        "process": [
            re.compile(r'\b(subprocess|os\.system|multiprocessing|threading|concurrent\.futures|sched|queue|signal|psutil|asyncio|time|atexit)\b', re.IGNORECASE)
        ]
    },
    'js': {
        "network": ["axios", "http", "https"],
        "file": ["fs", "path", "fs-extra"],
        "process": ["child_process", "exec", "spawn", "fork"]
    },
    'java': {
        "network": ["HttpURLConnection", "HttpClient", "Socket"],
        "file": ["File", "FileReader", "FileWriter"],
        "process": ["ProcessBuilder", "Runtime", "Thread"]
    }
}

# 특정 언어의 패턴을 불러오는 함수
def get_patterns(language):
    return PATTERNS.get(language, {})
