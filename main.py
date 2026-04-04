import customtkinter as ctk
import pandas as pd
from tkinter import filedialog, messagebox
import pyautogui
import time
import webbrowser

# Thiết lập giao diện tối
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class MessagingTool(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("TOOL GỬI TIN NHẮN HÀNG LOẠT")
        self.geometry("1000x600")
        self.duong_dan_excel = ""

        # Chia bố cục
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # 1. CỘT TRÁI - Menu điều khiển
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.btn_import = ctk.CTkButton(self.sidebar, text="CHỌN FILE DỮ LIỆU", fg_color="#1f538d", command=self.chon_file)
        self.btn_import.pack(pady=20, padx=10)

        self.btn_start = ctk.CTkButton(self.sidebar, text="BẮT ĐẦU GỬI", fg_color="green", command=self.bat_dau_gui)
        self.btn_start.pack(pady=10, padx=10)

        # 2. KHUNG GIỮA - Nội dung tin nhắn & Trạng thái
        self.main_content = ctk.CTkFrame(self)
        self.main_content.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        
        self.label_status = ctk.CTkLabel(self.main_content, text="Trạng thái: Đang chờ chọn file...", font=("Arial", 14))
        self.label_status.pack(pady=20)

    def chon_file(self):
        self.duong_dan_excel = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        if self.duong_dan_excel:
            self.label_status.configure(text=f"Đã chọn: {self.duong_dan_excel.split('/')[-1]}")
            messagebox.showinfo("Thông báo", "Đã tải danh sách thành công!")

    def bat_dau_gui(self):
        if not self.duong_dan_excel:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn file Excel trước!")
            return
        
        try:
            data = pd.read_excel(self.duong_dan_excel)
            messagebox.showinfo("Hướng dẫn", "Bạn có 5 giây để mở Zalo Desktop sau khi nhấn OK!")
            time.sleep(5)
            
            for index, row in data.iterrows():
                phone = str(row['Số điện thoại']).strip()
                name = str(row['Tên người nhận']).strip()
                message = f"Chào {name}, mình là Tuấn. Chúc bạn ngày mới tốt lành!"
                
                url = f"https://zalo.me/{phone}"
                webbrowser.open(url)
                time.sleep(5) # Đợi Zalo mở ô chat
                
                pyautogui.write(message)
                pyautogui.press('enter')
                time.sleep(10) # Nghỉ tránh spam
                
            self.label_status.configure(text="Trạng thái: Đã gửi xong toàn bộ!")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể gửi tin: {str(e)}")

if __name__ == "__main__":
    app = MessagingTool()
    app.mainloop()
