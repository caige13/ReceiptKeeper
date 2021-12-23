import base64
import pandas as pd

def create_onedrive_directdownload (onedrive_link):
    data_bytes64 = base64.b64encode(bytes(onedrive_link, 'utf-8'))
    data_bytes64_String = data_bytes64.decode('utf-8').replace('/','_').replace('+','-').rstrip("=")
    resultUrl = f"https://api.onedrive.com/v1.0/shares/u!{data_bytes64_String}/root/content"
    return resultUrl

onedrive_link = "https://1drv.ms/x/s!Am-Q4NBEyjKMkRvQxEGHiwWE0C_4?e=Wx8pFS"
onedrive_link = create_onedrive_directdownload(onedrive_link)
df = pd.read_excel(onedrive_link)
print(df)

df = df['col1']
df.to_excel(onedrive_link)