# streamlit_chrome_monitor.py
import streamlit as st
import psutil
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

CHROME_PROCESS_NAME = 'chrome.exe'
MEMORY_THRESHOLD_MB = 1024

def get_chrome_processes():
    chrome_processes = []
    for proc in psutil.process_iter():
        try:
            if proc.name() == CHROME_PROCESS_NAME:
                rss_mb = proc.memory_info().rss / (1024 * 1024)
                chrome_processes.append({
                    'PID': proc.pid,
                    'Memory_MB': rss_mb
                })
        except:
            continue
    return sorted(chrome_processes, key=lambda x: x['Memory_MB'], reverse=True)

st.title("🧠 Chrome Memory Usage Monitor")

if st.button("Scan Chrome Memory Usage"):
    process_data = get_chrome_processes()
    if process_data:
        df = pd.DataFrame(process_data)
        total_usage = df['Memory_MB'].sum()

        st.subheader("🔍 Chrome Processes")
        st.dataframe(df)

        st.metric("💾 Total Memory Usage (MB)", f"{total_usage:.2f}")

        if total_usage > MEMORY_THRESHOLD_MB:
            st.error(f"⚠️ Usage exceeds threshold ({MEMORY_THRESHOLD_MB} MB)!")
        else:
            st.success("Memory usage is within limits ✅")
    else:
        st.warning("No Chrome processes found.")

