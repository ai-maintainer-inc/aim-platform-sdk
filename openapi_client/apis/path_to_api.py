import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.agents_tickets import AgentsTickets
from openapi_client.apis.paths.agents_bids import AgentsBids
from openapi_client.apis.paths.agents_artifacts import AgentsArtifacts
from openapi_client.apis.paths.users_tickets import UsersTickets
from openapi_client.apis.paths.users import Users
from openapi_client.apis.paths.agents import Agents

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.AGENTS_TICKETS: AgentsTickets,
        PathValues.AGENTS_BIDS: AgentsBids,
        PathValues.AGENTS_ARTIFACTS: AgentsArtifacts,
        PathValues.USERS_TICKETS: UsersTickets,
        PathValues.USERS: Users,
        PathValues.AGENTS: Agents,
    }
)

path_to_api = PathToApi(
    {
        PathValues.AGENTS_TICKETS: AgentsTickets,
        PathValues.AGENTS_BIDS: AgentsBids,
        PathValues.AGENTS_ARTIFACTS: AgentsArtifacts,
        PathValues.USERS_TICKETS: UsersTickets,
        PathValues.USERS: Users,
        PathValues.AGENTS: Agents,
    }
)
