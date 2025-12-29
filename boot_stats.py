import psutil
import sqlite3
import datetime

# ------------ GET CURRENT STATS ------------
def get_stats():
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    return {
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cpu": psutil.cpu_percent(interval=1),
        "ram": ram.percent,
        "disk": disk.percent
    }

# ------------ SQL LOGIC ------------
def init_db():
    conn = sqlite3.connect("system_logs.db")
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS system_stats (
        time TEXT,
        cpu REAL,
        ram REAL,
        disk REAL
    )
    """)
    conn.commit()
    conn.close()

def get_last_stats():
    conn = sqlite3.connect("system_logs.db")
    c = conn.cursor()
    c.execute("SELECT cpu, ram, disk FROM system_stats ORDER BY time DESC LIMIT 1")
    result = c.fetchone()
    conn.close()
    return result

def save_stats(stats):
    conn = sqlite3.connect("system_logs.db")
    c = conn.cursor()
    c.execute("INSERT INTO system_stats VALUES (?, ?, ?, ?)",
              (stats["time"], stats["cpu"], stats["ram"], stats["disk"]))
    conn.commit()
    conn.close()

# ------------ DIFF FORMAT ------------
def format_diff(current, last):
    if last is None:
        return ""
    diff = current - last
    arrow = "▲" if diff > 0 else "▼" if diff < 0 else "•"
    return f" ({arrow} {abs(round(diff,1))}%)"

# ------------ MAIN EXECUTION ------------
init_db()
current = get_stats()
last = get_last_stats()

cpu_diff = format_diff(current["cpu"], last[0] if last else None)
ram_diff = format_diff(current["ram"], last[1] if last else None)
disk_diff = format_diff(current["disk"], last[2] if last else None)

report = f"""
🟣 Boot System Metrics
CPU: {current['cpu']}%{cpu_diff}
RAM: {current['ram']}%{ram_diff}
Disk: {current['disk']}%{disk_diff}
""".strip()

# Optional console-print if you run manually
print(report)

save_stats(current)
