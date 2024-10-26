employees = []


def display_menu():
    print("\n--- 人事資料管理系統 ---")
    print("1. 新增資料")
    print("2. 查詢資料")
    print("3. 修改資料")
    print("4. 刪除資料")
    print("5. 顯示所有資料")
    print("6. 退出系統")
    print("------------------------")


def add_employee():
    while True:
        department = input("請輸入部門: ")
        name = input("請輸入姓名: ")
        age = input("請輸入年齡: ")
        phone = input("請輸入手機號碼: ")

        employees.append({"部門": department, "姓名": name, "年齡": age, "手機": phone})

        other = input("是否繼續新增資料? (y/n): ")
        if other.lower() != 'y':
            break


def search_employee():
    name = input("請輸入要查詢的姓名: ")
    results = [emp for emp in employees if emp["姓名"] == name]
    if results:
        print("--- 查詢結果 ---")
        display_table(results)
    else:
        print("查無此人。")


def modify_employee():
    name = input("請輸入要修改的姓名: ")
    for emp in employees:
        if emp["姓名"] == name:
            print("當前資料:")
            display_table([emp])
            print("1. 修改部門")
            print("2. 修改姓名")
            print("3. 修改年齡")
            print("4. 修改手機")
            choice = input("請選擇要修改的欄位: ")
            if choice == "1":
                emp["部門"] = input("請輸入新的部門: ")
            elif choice == "2":
                emp["姓名"] = input("請輸入新的姓名: ")
            elif choice == "3":
                emp["年齡"] = input("請輸入新的年齡: ")
            elif choice == "4":
                emp["手機"] = input("請輸入新的手機: ")
            print("--- 更新後的資料 ---")
            display_table([emp])
            return
    print("查無此人。")


def delete_employee():
    name = input("請輸入要刪除的姓名: ")
    for emp in employees:
        if emp["姓名"] == name:
            confirm = input(f"確定要刪除 {name} 的資料嗎? (y/n): ")
            if confirm.lower() == 'y':
                employees.remove(emp)
                print(f"{name} 的資料已刪除。")
                after_delete_display_all_employees()
            return
    print("查無此人。")


def display_table(data):
    header = ["部門", "姓名", "年齡", "手機"]
    widths = [9, 8, 6, 15]
    print("\n" + "".join(header[i].ljust(widths[i]) for i in range(len(header))))
    print("-" * sum(widths))
    for emp in data:
        row = f"{emp['部門'].ljust(widths[0] - 1)}{emp['姓名'].ljust(widths[1])}{emp['年齡'].ljust(widths[2] + 1)}{emp['手機'].ljust(widths[3])}"
        print(row)


def display_all_employees():
    if employees:
        display_table(employees)
    else:
        print("目前沒有任何資料。")


def after_delete_display_all_employees():
    if employees:
        print("--- 剩餘的所有資料 ---")
        display_table(employees)
    else:
        print("目前沒有任何資料。")


def main():
    while True:
        display_menu()
        choice = input("請選擇功能: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            search_employee()
        elif choice == "3":
            modify_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            display_all_employees()
        elif choice == "6":
            print("系統已退出。")
            break
        else:
            print("無效選項，請重新輸入。")


if __name__ == "__main__":
    main()
