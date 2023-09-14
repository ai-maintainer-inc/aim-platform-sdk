import typing_extensions

from aim_platform_sdk.paths import PathValues
from aim_platform_sdk.apis.paths.agents_tickets import AgentsTickets
from aim_platform_sdk.apis.paths.agents_bids import AgentsBids
from aim_platform_sdk.apis.paths.agents_artifacts import AgentsArtifacts
from aim_platform_sdk.apis.paths.users_tickets import UsersTickets
from aim_platform_sdk.apis.paths.users_bids import UsersBids
from aim_platform_sdk.apis.paths.users_artifacts import UsersArtifacts
from aim_platform_sdk.apis.paths.users import Users
from aim_platform_sdk.apis.paths.agents import Agents
from aim_platform_sdk.apis.paths.repositories import Repositories
from aim_platform_sdk.apis.paths.users_benchmarks import UsersBenchmarks
from aim_platform_sdk.apis.paths.agents_benchmarks import AgentsBenchmarks

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.AGENTS_TICKETS: AgentsTickets,
        PathValues.AGENTS_BIDS: AgentsBids,
        PathValues.AGENTS_ARTIFACTS: AgentsArtifacts,
        PathValues.USERS_TICKETS: UsersTickets,
        PathValues.USERS_BIDS: UsersBids,
        PathValues.USERS_ARTIFACTS: UsersArtifacts,
        PathValues.USERS: Users,
        PathValues.AGENTS: Agents,
        PathValues.REPOSITORIES: Repositories,
        PathValues.USERS_BENCHMARKS: UsersBenchmarks,
        PathValues.AGENTS_BENCHMARKS: AgentsBenchmarks,
    }
)

path_to_api = PathToApi(
    {
        PathValues.AGENTS_TICKETS: AgentsTickets,
        PathValues.AGENTS_BIDS: AgentsBids,
        PathValues.AGENTS_ARTIFACTS: AgentsArtifacts,
        PathValues.USERS_TICKETS: UsersTickets,
        PathValues.USERS_BIDS: UsersBids,
        PathValues.USERS_ARTIFACTS: UsersArtifacts,
        PathValues.USERS: Users,
        PathValues.AGENTS: Agents,
        PathValues.REPOSITORIES: Repositories,
        PathValues.USERS_BENCHMARKS: UsersBenchmarks,
        PathValues.AGENTS_BENCHMARKS: AgentsBenchmarks,
    }
)
