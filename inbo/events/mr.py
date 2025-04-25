from __future__ import annotations
from typing import Any, List, Literal, TypeAlias, TypedDict
from datetime import datetime

class GLWebhookMREventData(TypedDict):
    assignees: List[AssigneeOrUser]
    changes: Changes
    event_type: str
    labels: List[Any]
    object_attributes: ObjectAttributes
    object_kind: str
    project: ProjectOrTargetOrSource
    repository: Repository
    user: AssigneeOrUser

class Changes(TypedDict):
    pass

MRAction : TypeAlias = Literal["open", "close", "reopen", "update", "approved", "unapproved", "approval", "unapproval", "merge"]

class ObjectAttributes(TypedDict):
    action: MRAction
    approval_rules: List[Any]
    assignee_id: int
    assignee_ids: List[int]
    author_id: int
    blocking_discussions_resolved: bool
    created_at: datetime
    description: str
    detailed_merge_status: str
    draft: bool
    first_contribution: bool
    head_pipeline_id: int
    human_time_change: None
    human_time_estimate: None
    human_total_time_spent: None
    id: int
    iid: int
    labels: List[Any]
    last_commit: LastCommit
    last_edited_at: None
    last_edited_by_id: None
    merge_commit_sha: str
    merge_error: None
    merge_params: MergeParams
    merge_status: str
    merge_user_id: None
    merge_when_pipeline_succeeds: bool
    milestone_id: None
    prepared_at: datetime
    reviewer_ids: List[Any]
    source: ProjectOrTargetOrSource
    source_branch: str
    source_project_id: int
    state: str
    state_id: int
    target: ProjectOrTargetOrSource
    target_branch: str
    target_project_id: int
    time_change: int
    time_estimate: int
    title: str
    total_time_spent: int
    updated_at: datetime
    updated_by_id: None
    url: str
    work_in_progress: bool

class LastCommit(TypedDict):
    author: Author
    id: str
    message: str
    timestamp: datetime
    title: str
    url: str

class Author(TypedDict):
    email: str
    name: str

class MergeParams(TypedDict):
    force_remove_source_branch: str
    should_remove_source_branch: bool

class ProjectOrTargetOrSource(TypedDict):
    avatar_url: None
    ci_config_path: None
    default_branch: str
    description: str
    git_http_url: str
    git_ssh_url: str
    homepage: str
    http_url: str
    id: int
    name: str
    namespace: str
    path_with_namespace: str
    ssh_url: str
    url: str
    visibility_level: int
    web_url: str

class Repository(TypedDict):
    description: str
    homepage: str
    name: str
    url: str

class AssigneeOrUser(TypedDict):
    avatar_url: str
    email: str
    id: int
    name: str
    username: str
