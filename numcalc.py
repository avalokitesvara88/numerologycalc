import streamlit as st
import datetime as dt
from datetime import date, timedelta

st.title("Numerology Calculator")

default_date = dt.date(2025, 3, 21)
min_date = dt.date(1900, 1, 1)
max_date = dt.date(2100, 1, 1)


def daterange(s_date: date, e_date: date):
    days = int((e_date - s_date).days)
    for n in range(days):
        yield s_date + timedelta(n)


def singledigit(n):
    _sum = 0
    mn = False
    # Repetitively calculate sum until
    # it becomes single digit
    if n == 11:
        mn = True
        _sum = 11
    if n == 22:
        mn = True
        _sum = 22
    if n == 33:
        mn = True
        _sum = 33

    while (n > 0 or _sum > 9) and not mn:
        # If n becomes 0, reset it to sum
        # and start a new iteration
        # if _sum == (11 or 22 or 33 or 28) or
        if n == 0:
            n = _sum
            _sum = 0
        _sum += n % 10
        n //= 10
        if _sum == 11:
            # _sum = 11
            mn = True
        if _sum == 22:
            # _sum = 22
            mn = True
        if _sum == 33:
            # _sum = 33
            mn = True
    return _sum


def calcpath(p_start, p_end, p_lifepath=28, p_birthnumber=28, lp=False, bn=False):
    if p_start > p_end:
        st.warning("End Date Should be Greater than Start Date")
    else:
        for single_date in daterange(p_start, p_end):
            pt1 = str(single_date).split('-')
            y1 = singledigit(int(pt1[0]))
            m1 = singledigit(int(pt1[1]))
            d1 = singledigit(int(pt1[2]))
            lp = singledigit(y1 + m1 + d1)
            if p_birthnumber == 28 and int(pt1[2]) == 28 and (lp and bn):
                d1 = 28
                lp = singledigit(y1 + m1 + 1)

            if lp == p_lifepath and lp and not bn:
                st.write(single_date.strftime("%d-%m-%Y") + f" LP:{lp} Day:{d1} Year: {y1}")

            if lp == p_lifepath and d1 == p_birthnumber and (lp and bn):
                st.write(single_date.strftime("%d-%m-%Y") + f" LP:{lp} Day:{d1} Year: {y1}")


with st.form(key="get_lp"):
    start_date = st.date_input("Staring Date", value=default_date, min_value=min_date, max_value=max_date)
    end_date = st.date_input("Ending Date", value=default_date, min_value=min_date, max_value=max_date)
    life_path = st.number_input("Enter Desired LifePath", value=28)
    submit_button = st.form_submit_button("Calculate LP")
    if submit_button:
        calcpath(start_date, end_date, life_path, lp=True, bn=False)

with st.form(key="get_date_lp"):
    start_date = st.date_input("Staring Date", value=default_date, min_value=min_date, max_value=max_date)
    end_date = st.date_input("Ending Date", value=default_date, min_value=min_date, max_value=max_date)
    life_path = st.number_input("Enter Desired LifePath", value=28)
    birth_num = st.number_input("Enter Desired Birth Number", value=28)
    submit_button = st.form_submit_button("Calculate LP")
    if submit_button:
        calcpath(start_date, end_date, p_lifepath=life_path, p_birthnumber=birth_num, lp=True, bn=True)
