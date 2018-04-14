import repositorie
import issue
import comments

issues_olds = issue.get_only_issues_more_fifteen_days(repositorie.get_issue_repo())
# comments = comments.get_last_comment_issue_and_analisy(issues_olds)
