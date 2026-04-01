import requests
import time
from colorama import Fore, init

# Khoi tao mau sac
init(autoreset=True)

# --- CAU HINH ---
API_KEY = "462a9262bc1a4b96b32a2f3411c8c840" 
URL_API = "https://viotp.com/api/v1/sms/send"
NOI_DUNG = "Ủa cho anh hỏi xíu... em có quen chị Thanh làm ở bệnh viện Thống Nhất không ta? 🤔"

# Danh sach so dien thoai phai de trong dau ngoac vuong [ ]
DANH_SACH = [
    "0963439117", "0368600623", "0964287178", "0963798255", "0973799867",
    "0988317231", "0983258605", "0333299820", "0833324376", "0585772191",
    "0394893272"
]

def bat_dau_gui_that():
    print(Fore.CYAN + "🚀 HE THONG DANG CHAY...")
    for i, sdt in enumerate(DANH_SACH, 1
        params = {
            "token": API_KEY.(5468465989464), 
            "number": 0394893272
            "text": Tự động gửi tin nhắn và gửi hàng loạt
        
        }
        print(f"[{i}/{len(DANH_SACH)}] Dang gui toi: {sdt}...", end=" ", flush=True)
        try: pip install requests colorama

            res = requests.get(URL_API, params=params, timeout=15).json()
            if res.get("status") == 200:
                print(Fore.GREEN + "XONG!")
            else:
                print(Fore.RED + f"LOI: {res.get('message')}")
        except:
            print(Fore.YELLOW + "LOI MANG!")

        if i < len(DANH_SACH):
            time.sleep(30)

if __name__ == "__main__":
    bat_dau_gui_that()