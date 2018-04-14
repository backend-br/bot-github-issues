#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import time

def get_only_issues_more_fifteen_days(issues):
    issues_olds = []
    for issue in issues:
        past = datetime.datetime.now() + datetime.timedelta(days=-15)
        
        if issue.created_at <= past:
            issues_olds.append(issue)

    return issues_olds