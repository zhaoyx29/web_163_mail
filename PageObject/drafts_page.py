# -*- coding: utf-8 -*-
# @Time    : 2018/11/10 14:26
# @Author  :  'zyx'
# @Email   : 458757014@qq.com
# @File    : MyLogger.py
# @Software: PyCharm Community Edition

from Common.BasePage import BasePage
from Common.my_log import logger
from PageLocator.drafts_locator import DraftsLocator


class DraftsPage(DraftsLocator,BasePage):
    def get_today_draft_count(self):
        name="获取今日草稿的数目"
        return self.get_text(self.today_draft_count,model_name=name)