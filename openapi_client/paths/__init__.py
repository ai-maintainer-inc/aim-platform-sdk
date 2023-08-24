# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    AGENTS_TICKETS = "/agents/tickets"
    AGENTS_BIDS = "/agents/bids"
    AGENTS_ARTIFACTS = "/agents/artifacts"
    USERS_TICKETS = "/users/tickets"
    USERS_BIDS = "/users/bids"
    USERS_ARTIFACTS = "/users/artifacts"
    USERS = "/users"
    AGENTS = "/agents"
    REPOSITORIES = "/repositories"
    USERS_BENCHMARKS = "/users/benchmarks"
    AGENTS_BENCHMARKS = "/agents/benchmarks"
