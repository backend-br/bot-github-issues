#!/usr/bin/env python
# -*- coding: utf-8 -*-

from github import Github
import settings

def get_issue_repo():
	g = Github(settings.ENV['USER_GITHUB'], settings.ENV['PSWD_GITHUB'])

	repo = g.get_organization(settings.ENV['ORGANIZATION_GITHUB']).get_repo(settings.ENV['REPO_GITHUB'])
	
	return repo.get_issues()