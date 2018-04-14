#!/usr/bin/env python
# -*- coding: utf-8 -*-

from github import Github
import settings

def get_last_comment_issue_and_analisy(issues):
    g = Github(settings.ENV['USER_GITHUB'], settings.ENV['PSWD_GITHUB'])

    repo = g.get_organization(settings.ENV['ORGANIZATION_GITHUB']).get_issues_comments('vagas')

    print(repo)