# -*- coding: utf-8 -*-

from datetime import date, datetime, time, timedelta

'''
TODO: 统一命名函数名字，YYYYMMDD 统一改为 YYYYmmdd，int 改为 ms
'''


def now_for_log_str():
    return datetime.now().strftime('%Y%m%d-%H:%M:%S.%f')[:-3]


def now_2_YYYYMMDD():
    return datetime.today().strftime('%Y%m%d')


def timestamp_2_YYYYMMDD(timestamp_in_milliseconds: int) -> str:
    return datetime.fromtimestamp(timestamp_in_milliseconds/1000).strftime('%Y%m%d')


def get_last_thursday() -> date:
    '''
    get the date of last thursday
    '''
    today = datetime.today()
    offset = (today.weekday() - 3) % 7
    last_thursday = today - timedelta(days=offset)
    return last_thursday


def yyyymmdd_2_int(yyyymmdd: str) -> int:
    '''
    返回对应时间的毫秒值
    '''
    return int(datetime.strptime(yyyymmdd, '%Y%m%d').timestamp()) * 1000


def get_next_day_in_YYYYMMDD(ms: int):
    '''
    ms这个时间点之后一天的日期，ms单位是毫秒
    '''
    return datetime.fromtimestamp(ms/1000 + 3600 * 24).strftime('%Y%m%d')
