"""
@Description :   轨缝计算
@Author      :   ZhengJiaheng
@Time        :   2024/08/21 21:37:45
"""

def guifengjisuan():
    # 轨缝计算类型选择
    old_line = "更换钢轨预留轨缝计算(既有线)"
    new_line = "新线铺轨预留轨缝计算（新线施工）"

    while True:
        try:
            first_choose = input(f"请选择施工类型:\n\t1:{old_line}\n\t2:{new_line}\n请在此输入:")
            if first_choose == "1":
                # 更换钢轨预留轨缝计算(既有线)
                url = "https://www.guimei8.com/723.html"
                print(f"参考网址: {url}")
                
                A = 0.0118  # 钢轨膨胀系数
                l = float(input("请输入钢轨长度，单位:m"))
                Tmax = float(input("请输入当地历史最高轨温 Tmax:"))
                Tmin = float(input("请输入当地历史最低轨温 Tmin:"))
                Tz = float(input("请输入更换钢轨或调整轨缝时温度 Tz:"))
                Ag_gouzaoguifeng = 18  # 50、60、75KG/m钢轨构造轨缝常数
                
                # 计算轨缝长度
                T0 = (Tmax + Tmin) / 2
                delta_T = T0 - Tz
                half_gouzaoguifeng = Ag_gouzaoguifeng / 2
                a0_guifeng = A * l * delta_T + half_gouzaoguifeng

                print(f"轨缝长度应为: {a0_guifeng:.2f} mm")
                break

            elif first_choose == "2":
                print("选择2")
                break
            else:
                print("选择有误，请输入1或2。")
        except ValueError:
            print("输入有误，请输入有效的数值。")

if __name__ == "__main__":
    guifengjisuan()
