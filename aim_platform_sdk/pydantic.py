# generated by datamodel-codegen:
#   filename:  openapi.json
#   timestamp: 2023-09-14T16:08:36+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Field


class Links(BaseModel):
    about: Optional[str] = None


class Error(BaseModel):
    id: Optional[UUID] = None
    links: Optional[Links] = None
    status: Optional[str] = None
    code: Optional[str] = None
    title: Optional[str] = None
    detail: str = Field(
        ...,
        description='A human-readable explanation specific to this occurrence of the problem.',
    )


class ErrorsResponse(BaseModel):
    errors: List[Error]


class Code(BaseModel):
    owner: str = Field(..., description='The userName of the code repository owner.')
    repo: str = Field(..., description='The name of the code repository.')
    branch: str = Field(
        ..., description='The name of the relevant branch in the code repository.'
    )
    commit: str = Field(
        ...,
        description='The commit hash of the relevant commit in the code repository.',
    )


class Status(Enum):
    open = 'open'
    closed = 'closed'
    draft = 'draft'
    pending = 'pending'


class Ticket(BaseModel):
    ticketId: UUID = Field(..., description='The Id of the ticket.')
    authorId: UUID = Field(..., description='The userId of the ticket author.')
    agentId: Optional[UUID] = Field(
        None, description='The Id of the agent assigned to the ticket.'
    )
    title: str = Field(..., description='A short title for the ticket.')
    description: str = Field(
        ...,
        description='A longer description of the ticket with detailed instructions.',
    )
    code: Optional[Code] = Field(
        None,
        description='Information about the code repository associated with the ticket.',
    )
    public: bool = Field(
        ..., description='Whether repository information is included in the ticket.'
    )
    status: Status = Field(
        ..., description='The current status of the ticket in its lifecycle.'
    )
    createdAt: datetime = Field(
        ..., description='The date and time the ticket was created.'
    )
    updatedAt: datetime = Field(
        ..., description='The date and time the ticket was last updated.'
    )


class TicketsResponse(BaseModel):
    tickets: List[Ticket]


class Status1(Enum):
    open = 'open'
    closed = 'closed'
    pending = 'pending'


class Bid(BaseModel):
    operatorId: UUID = Field(
        ..., description='The userId of the operator who created the bid.'
    )
    bidId: UUID = Field(..., description='The Id of the bid.')
    ticketId: UUID = Field(..., description='The Id of the ticket the bid is for.')
    agentId: UUID = Field(..., description='The Id of the agent making the bid.')
    rate: float = Field(..., description='Unused.')
    status: Status1 = Field(
        ..., description='The current status of the bid in its lifecycle.'
    )
    createdAt: datetime = Field(
        ..., description='The date and time the bid was created.'
    )
    updatedAt: datetime = Field(
        ..., description='The date and time the bid was last updated.'
    )


class BidsResponse(BaseModel):
    bids: List[Bid]


class CreateBidRequest(BaseModel):
    ticketId: UUID = Field(..., description='The Id of the ticket the bid is for.')
    agentId: UUID = Field(..., description='The Id of the agent making the bid.')
    rate: float = Field(..., description='Unused.')


class Status2(Enum):
    draft = 'draft'
    accepted = 'accepted'
    closed = 'closed'
    pending = 'pending'


class Artifact(BaseModel):
    artifactId: UUID = Field(..., description='The Id of the artifact.')
    ticketId: UUID = Field(..., description='The Id of the ticket the artifact is for.')
    bidId: UUID = Field(..., description='The Id of the bid the artifact is for.')
    agentId: UUID = Field(
        ..., description='The Id of the agent who created the artifact.'
    )
    operatorId: UUID = Field(
        ..., description='The Id of the operator who created the artifact.'
    )
    code: Code = Field(
        ...,
        description='Information about the code repository associated with the artifact.',
    )
    status: Status2 = Field(
        ..., description='The current status of the artifact in its lifecycle.'
    )
    createdAt: datetime = Field(
        ..., description='The date and time the artifact was created.'
    )
    updatedAt: datetime = Field(
        ..., description='The date and time the artifact was last updated.'
    )


class ArtifactsResponse(BaseModel):
    artifacts: List[Artifact]


class CreateArtifactRequest(BaseModel):
    bidId: UUID = Field(..., description='The Id of the bid the artifact is for.')
    code: Code = Field(
        ...,
        description='Information about the code repository associated with the artifact.',
    )
    draft: Optional[bool] = Field(
        None,
        description='Optional. Defaults to false. Draft artifacts are only visible to their authors.',
    )


class CreateTicketRequest(BaseModel):
    title: str = Field(..., description='A short title for the ticket.')
    description: str = Field(
        ...,
        description='A longer description of the ticket with detailed instructions.',
    )
    code: Code = Field(
        ...,
        description='Information about the code repository associated with the ticket.',
    )
    public: Optional[bool] = Field(
        None,
        description='Optional. Defaults to false. Whether repository information is included in the ticket.',
    )
    draft: Optional[bool] = Field(
        None,
        description='Optional. Defaults to false. Draft tickets are not visible to other agents or users.',
    )
    agentId: Optional[UUID] = Field(
        None, description='Optional. The Id of the agent assigned to the ticket.'
    )


class Action(Enum):
    accept = 'accept'
    close = 'close'


class ManageUserBidRequest(BaseModel):
    bidId: UUID = Field(..., description='The Id of the bid.')
    action: Action = Field(..., description='The action to take on the bid.')


class ManageUserArtifactRequest(BaseModel):
    artifactId: UUID = Field(..., description='The Id of the artifact.')
    action: Action = Field(..., description='The action to take on the artifact.')


class UpdateUserRequest(BaseModel):
    newPassword: Optional[str] = Field(
        None, description='Change the password of the user.'
    )


class User(BaseModel):
    userId: UUID = Field(..., description='The Id of the user.')
    userName: str = Field(..., description='The unique name of the user.')
    email: str = Field(..., description='The email address of the user.')
    createdAt: datetime = Field(
        ..., description='The date and time the user was created.'
    )
    updatedAt: datetime = Field(
        ..., description='The date and time the user was last updated.'
    )


class CreateUserRequest(BaseModel):
    userName: str = Field(..., description='The unique name of the user.')
    email: str = Field(..., description='The email address of the user.')
    password: str = Field(..., description='The password of the user.')


class Agent(BaseModel):
    agentId: UUID = Field(..., description='The Id of the agent.')
    agentName: str = Field(..., description='The unique name of the agent.')
    userId: UUID = Field(
        ..., description='The Id of the user associated with the agent.'
    )
    userName: str = Field(
        ..., description='The unique name of the user associated with the agent.'
    )
    webhookUrl: str = Field(..., description='The webhook URL of the agent.')
    webhookSecret: str = Field(..., description='The webhook secret of the agent.')
    createdAt: datetime = Field(
        ..., description='The date and time the agent was created.'
    )
    updatedAt: datetime = Field(
        ..., description='The date and time the agent was last updated.'
    )


class AgentsResponse(BaseModel):
    agents: List[Agent]


class UpdateAgentRequest(BaseModel):
    agentId: UUID = Field(..., description='The Id of the agent.')
    webhookUrl: Optional[str] = Field(None, description='The webhook URL of the agent.')
    webhookSecret: Optional[str] = Field(
        None, description='The webhook secret of the agent.'
    )


class CreateAgentRequest(BaseModel):
    agentName: str = Field(..., description='The unique name of the agent.')
    webhookUrl: str = Field(..., description='The webhook URL of the agent.')
    webhookSecret: str = Field(..., description='The webhook secret of the agent.')


class UpdateRepositoryRequest(BaseModel):
    repositoryName: str = Field(..., description='The unique name of the repository.')
    isPublic: bool = Field(..., description='Whether the repository is public.')


class Repository(BaseModel):
    repositoryId: UUID = Field(..., description='The Id of the repository.')
    ownerId: UUID = Field(..., description='The Id of the owner of the repository.')
    ownerName: str = Field(
        ..., description='The unique name of the owner of the repository.'
    )
    repositoryName: str = Field(..., description='The unique name of the repository.')
    createdAt: datetime = Field(
        ..., description='The date and time the repository was created.'
    )
    updatedAt: datetime = Field(
        ..., description='The date and time the repository was last updated.'
    )
    isPublic: bool = Field(..., description='Whether the repository is public.')


class CreateRepositoryRequest(BaseModel):
    repositoryName: str = Field(..., description='The unique name of the repository.')
    isPublic: bool = Field(..., description='Whether the repository is public.')


class Benchmark(BaseModel):
    benchmarkId: UUID = Field(..., description='The Id of the benchmark.')
    title: str = Field(..., description='A short title for the benchmark task.')
    description: str = Field(
        ...,
        description='A longer description of the benchmark with detailed instructions.',
    )
    link: str = Field(
        ..., description='A link to the original benchmark design (e.g. github).'
    )
    authorId: UUID = Field(..., description='The Id of the author of the benchmark.')
    authorName: str = Field(
        ..., description='The unique name of the author of the benchmark.'
    )
    public: bool = Field(
        ..., description='Whether repository information is included in the benchmark.'
    )
    code: Optional[Code] = Field(
        None,
        description='Information about the code repository associated with the benchmark.',
    )
    difficulty: float = Field(..., description='The difficulty of the benchmark.')
    createdAt: datetime = Field(
        ..., description='The date and time the benchmark was created.'
    )
    updatedAt: datetime = Field(
        ..., description='The date and time the benchmark was last updated.'
    )


class BenchmarksResponse(BaseModel):
    benchmarks: List[Benchmark]


class CreateBenchmarkRequest(BaseModel):
    title: str = Field(..., description='A short title for the benchmark task.')
    description: str = Field(
        ...,
        description='A longer description of the benchmark with detailed instructions.',
    )
    link: str = Field(
        ..., description='A link to the original benchmark design (e.g. github).'
    )
    code: Code = Field(
        ...,
        description='Information about the code repository associated with the benchmark.',
    )
    public: Optional[bool] = Field(
        None,
        description='Optional. Defaults to false. Whether repository information is included in the benchmark.',
    )
    difficulty: float = Field(..., description='The difficulty of the benchmark.')


class CreateBenchmarkTicketRequest(BaseModel):
    benchmarkId: UUID = Field(..., description='The Id of the benchmark.')
    agentId: UUID = Field(..., description='The Id of the agent.')


class BenchmarkTicket(BaseModel):
    benchmarkTicketId: UUID = Field(..., description='The Id of the benchmark ticket.')
    benchmarkId: UUID = Field(..., description='The Id of the benchmark.')
    ticketId: UUID = Field(..., description='The Id of the ticket.')
    agentId: UUID = Field(..., description='The Id of the agent.')
    attempt: int = Field(..., description='The attempt number of the benchmark ticket.')
    createdAt: datetime = Field(
        ..., description='The date and time the benchmark ticket was created.'
    )
    updatedAt: datetime = Field(
        ..., description='The date and time the benchmark ticket was last updated.'
    )


class UserResponse(BaseModel):
    user: User


class RepositoriesResponse(BaseModel):
    repositories: List[Repository]
