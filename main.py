from tkinterdnd2 import TkinterDnD
from ui_window import MonGenUI

if __name__ == "__main__":
    # 使用 TkinterDnD.Tk 替代普通的 tk.Tk，以支持拖拽功能
    root = TkinterDnD.Tk()
    app = MonGenUI(root)
    root.mainloop()

#pip install tkinterdnd2    