from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_credentials_rotate_response import AgentCredentialsRotateResponse
from ...models.error import Error
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/agent/credentials/rotate",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AgentCredentialsRotateResponse | Error | None:
    if response.status_code == 201:
        response_201 = AgentCredentialsRotateResponse.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AgentCredentialsRotateResponse | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[AgentCredentialsRotateResponse | Error]:
    """Rotate the calling agent PAT

     Atomically mints a successor personal access token for the one that authenticated this request. A
    machine account has no password and no usable mailbox, so this is its only way to rotate a leaked
    credential. The successor keeps the predecessor's scopes, billing_enabled flag, name, client_label,
    and expiry policy; only the secret changes. The predecessor is not revoked at once. It stays in a
    grace period that ends at the successor's first successful request or one hour after the rotation,
    whichever comes first. During that period it authenticates only this route, and every other route
    answers it with a bare 401. If the 201 is lost, call this route again with the predecessor while the
    successor is still unused: the response carries the same pat_id and a NEW secret, and the earlier
    successor secret stops working. Keep the predecessor until the successor has made one successful
    call, because a late-landing earlier retry can replace the successor's secret. Then make one call
    with the successor right away to retire the predecessor. Once the successor has been used or the
    hour has passed, the predecessor is refused here as well. This route references no token but the one
    that called it and that token's own successor: it cannot list, mint, or revoke any other credential.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentCredentialsRotateResponse | Error]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> AgentCredentialsRotateResponse | Error | None:
    """Rotate the calling agent PAT

     Atomically mints a successor personal access token for the one that authenticated this request. A
    machine account has no password and no usable mailbox, so this is its only way to rotate a leaked
    credential. The successor keeps the predecessor's scopes, billing_enabled flag, name, client_label,
    and expiry policy; only the secret changes. The predecessor is not revoked at once. It stays in a
    grace period that ends at the successor's first successful request or one hour after the rotation,
    whichever comes first. During that period it authenticates only this route, and every other route
    answers it with a bare 401. If the 201 is lost, call this route again with the predecessor while the
    successor is still unused: the response carries the same pat_id and a NEW secret, and the earlier
    successor secret stops working. Keep the predecessor until the successor has made one successful
    call, because a late-landing earlier retry can replace the successor's secret. Then make one call
    with the successor right away to retire the predecessor. Once the successor has been used or the
    hour has passed, the predecessor is refused here as well. This route references no token but the one
    that called it and that token's own successor: it cannot list, mint, or revoke any other credential.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentCredentialsRotateResponse | Error
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[AgentCredentialsRotateResponse | Error]:
    """Rotate the calling agent PAT

     Atomically mints a successor personal access token for the one that authenticated this request. A
    machine account has no password and no usable mailbox, so this is its only way to rotate a leaked
    credential. The successor keeps the predecessor's scopes, billing_enabled flag, name, client_label,
    and expiry policy; only the secret changes. The predecessor is not revoked at once. It stays in a
    grace period that ends at the successor's first successful request or one hour after the rotation,
    whichever comes first. During that period it authenticates only this route, and every other route
    answers it with a bare 401. If the 201 is lost, call this route again with the predecessor while the
    successor is still unused: the response carries the same pat_id and a NEW secret, and the earlier
    successor secret stops working. Keep the predecessor until the successor has made one successful
    call, because a late-landing earlier retry can replace the successor's secret. Then make one call
    with the successor right away to retire the predecessor. Once the successor has been used or the
    hour has passed, the predecessor is refused here as well. This route references no token but the one
    that called it and that token's own successor: it cannot list, mint, or revoke any other credential.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentCredentialsRotateResponse | Error]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> AgentCredentialsRotateResponse | Error | None:
    """Rotate the calling agent PAT

     Atomically mints a successor personal access token for the one that authenticated this request. A
    machine account has no password and no usable mailbox, so this is its only way to rotate a leaked
    credential. The successor keeps the predecessor's scopes, billing_enabled flag, name, client_label,
    and expiry policy; only the secret changes. The predecessor is not revoked at once. It stays in a
    grace period that ends at the successor's first successful request or one hour after the rotation,
    whichever comes first. During that period it authenticates only this route, and every other route
    answers it with a bare 401. If the 201 is lost, call this route again with the predecessor while the
    successor is still unused: the response carries the same pat_id and a NEW secret, and the earlier
    successor secret stops working. Keep the predecessor until the successor has made one successful
    call, because a late-landing earlier retry can replace the successor's secret. Then make one call
    with the successor right away to retire the predecessor. Once the successor has been used or the
    hour has passed, the predecessor is refused here as well. This route references no token but the one
    that called it and that token's own successor: it cannot list, mint, or revoke any other credential.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentCredentialsRotateResponse | Error
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
