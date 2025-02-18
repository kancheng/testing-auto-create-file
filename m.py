import os
import time
from datetime import datetime

def create_directory_if_not_exists():
    # 取得當前日期
    today = datetime.today().strftime('%Y%m%d')
    # 檢查是否存在當日目錄
    if not os.path.exists(today):
        os.makedirs(today)
    return today

def create_txt_file(directory):
    # 取得當前時間，並以年月日時分秒作為檔名
    current_time = datetime.now().strftime('%Y%m%d%H%M%S')
    file_name = f"{directory}/{current_time}.txt"
    
    # 創建檔案並寫入隨意內容
    with open(file_name, 'w') as file:
        file.write("這是測試內容。\n")
    
    print(f"檔案已建立: {file_name}")

def main():
    while True:
        # 確保當日目錄存在
        today_directory = create_directory_if_not_exists()
        
        # 每 10 分鐘創建一個 txt 檔案
        create_txt_file(today_directory)
        
        # 等待 10 分鐘
        time.sleep(600)

if __name__ == "__main__":
    main()
