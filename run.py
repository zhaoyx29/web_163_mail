# -*- coding: utf-8 -*-

import pytest
import time

pytest.main(["-m","smoke","--reruns","2","--html=Reports\\{0}_report.html".format(time.strftime("%Y%m%d_%H%M%S"))])
