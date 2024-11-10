# 언어별 패턴 정의
PATTERNS = {
    'rb': {
        "network": ["HTTParty", "Net", "Socket", "HTTP"],
        "file": ["File", "Dir", "Pathname", "FileUtils"],
        "process": ["Process", "exec", "system", "Thread"]
    },
    'py': {
        "network": ["requests", "http", "socket"],
        "file": ["os", "open", "shutil", "pathlib"],
        "process": ["subprocess", "os.system", "multiprocessing", "threading"]
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
