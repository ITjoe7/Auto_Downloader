import subprocess
import time

while True:
    # Run the WinSCP script
    winscp_path = r'C:\Program Files (x86)\WinSCP\WinSCP.com'
    winscp_script = r'C:\Users\Joren\Auto_Downloader\WinSCP_script.txt'
    subprocess.run([winscp_path, f'/script={winscp_script}'])
    
    #Loop
    time.sleep(15)  
