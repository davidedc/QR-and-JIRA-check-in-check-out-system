# This script shows how to use the client in anonymous mode
# against jira.atlassian.com.

from jira.client import JIRA

# By default, the client will connect to a JIRA instance started from the Atlassian Plugin SDK
# (see https://developer.atlassian.com/display/DOCS/Installing+the+Atlassian+Plugin+SDK for details).
# Override this with the options parameter.
options = {
    'server': 'JIRA URL'
}

jira = JIRA(options, basic_auth=('JIRA USERNAME', 'JIRA PASSWORD'))

# Get an issue.
issue = jira.issue('PUT HERE AN ISSUE IN YOUR SYSTEM')

#issue.update(assignee={'name': ''}) # this is to un-assign an issue
issue.update(assignee={'name': 'NAME OF A USER'})
jira.add_comment('ISSUE ID', 'new comment')