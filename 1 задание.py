if __name__ == '__main__':
    a_cost_month, b_megabite, c_pay_extra, d_all_megabite = list(map(int, input().split()))
    print(a_cost_month if d_all_megabite <= b_megabite else a_cost_month + (d_all_megabite-b_megabite)*c_pay_extra)
