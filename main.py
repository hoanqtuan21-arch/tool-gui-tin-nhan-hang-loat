import customtkinter as ctk

# Thiết lập giao diện tối
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class MessagingTool(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Cấu hình cửa sổ chính
        self.title("TOOL GỬI TIN NHẮN HÀNG LOẠT")
        self.geometry("1000x600")

        # Chia bố cục: Cột trái (Menu), Khung giữa (Nội dung), Cột phải (Trạng thái)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # 1. CỘT TRÁI - Menu điều khiển
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        
        self.btn_import = ctk.CTkButton(self.sidebar, text="CHÔN FILE DỮ LIỆU", fg_color="#1f538d")
        self.btn_import.pack(pady=20, padx=10)
        
        self.btn_contacts = ctk.CTkButton(self.sidebar, text="NHẬP LIÊN HỆ", fg_color="green")
        self.btn_contacts.pack(pady=10, padx=10)

        # 2. KHUNG GIỮA - Nội dung tin nhắn & Bảng dữ liệu
        self.main_content = ctk.CTkFrame(self)
        self.main_content.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.lbl_msg = ctk.CTkLabel(self.main_content, text="NỘI DUNG TIN NHẮN", font=("Arial", 14, "bold"))
        self.lbl_msg.pack(pady=(10, 0))
        
        self.txt_message = ctk.CTkTextbox(self.main_content, height=200)
        self.txt_message.pack(fill="x", padx=20, pady=10)

        # Mô phỏng bảng dữ liệu bên dưới
        self.data_table = ctk.CTkTextbox(self.main_content, height=250)
        self.data_table.insert("0.0", "STT | Số điện thoại | Nội dung | Trạng thái\n" + "-"*50)
        self.data_table.pack(fill="both", expand=True, padx=20, pady=10)

        # 3. CỘT PHẢI - Trạng thái gửi
        self.status_panel = ctk.CTkFrame(self, width=200)
        self.status_panel.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)
        
        self.lbl_stats = ctk.CTkLabel(self.status_panel, text="TRẠNG THÁI GỬI", font=("Arial", 14, "bold"))
        self.lbl_stats.pack(pady=20)
        
        # Vòng tròn trạng thái (giả lập số 0 lớn)
        self.circle_status = ctk.CTkLabel(self.status_panel, text="0", font=("Arial", 50), 
                                          width=120, height=120, fg_color="transparent", 
                                          border_width=5, corner_radius=60, border_color="green")
        self.circle_status.pack(pady=10)

        self.lbl_detail = ctk.CTkLabel(self.status_panel, text="Đã gửi: 0\nChờ: 0\nLỗi: 0", justify="left")
        self.lbl_detail.pack(pady=20)

        self.btn_start = ctk.CTkButton(self, text="BẮT ĐẦU GỬI", height=40, font=("Arial", 15, "bold"))
        self.btn_start.pack(side="bottom", pady=20)

if __name__ == "__main__":
    app = MessagingTool()
    app.mainloop()
