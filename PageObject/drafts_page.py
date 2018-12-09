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

    def checked_draft_content(self):
        name="选中要删除的草稿"
        logger.info(name)
        self.wait_eleVisibility(self.checkbox_draft,model_name=name)
        self.click_ele(self.checkbox_draft,model_name=name)

    def del_draft(self):
        name="删除草稿"
        logger.info(name)
        self.checked_draft_content()
        self.click_ele(self.del_draft_button,model_name=name)
