# -*- coding: utf-8 -*-

import mongoengine
from pandas import DataFrame
from quantz_repo import IndexDailyItem

from .utils import log

TAG = 'Repo'


class QuantzRepo(object):
    '''
    quant 数据仓库对外接口
    '''

    def __init__(self, db=None, **kwargs):
        mongoengine.connect(db, kwargs)

    def get_index_daily(self, code: str, trade_date: str = None, start_date: str = None, end_date: str = None):
        '''
        获取指数日线数据
        :param code: 指数代码
        :param trade_date: 交易日
        :param start_date: 起始日期
        :param end_date: 结束日期
        :return: DataFrame
        '''
        if code is None:
            log.w(TAG, 'code unspecified')
        else:
            pass

    def get_industry_classify(self, level: str = 'Lr', src: str = 'sw') -> DataFrame:
        """ 获取某个级别的行业分类

        :param level: 获取一二三级的行业分类， L1,L2,L3, defaults to 'L2'
        :type level: str, optional
        :param src: [description], defaults to 'sw'
        :type src: str, optional
        :return: [description]
        :rtype: DataFrame
        """
        pass
