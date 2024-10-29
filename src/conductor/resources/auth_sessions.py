# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import auth_session_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.auth_session import AuthSession

__all__ = ["AuthSessionsResource", "AsyncAuthSessionsResource"]


class AuthSessionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuthSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return AuthSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return AuthSessionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        end_user_id: str,
        publishable_key: str,
        link_expiry_mins: float | NotGiven = NOT_GIVEN,
        redirect_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthSession:
        """
        To launch the authentication flow, create an AuthSession and pass the returned
        session’s `authFlowUrl` to the client for your end-user to visit in their
        browser.

        Args:
          end_user_id: The ID of the EndUser for whom to create the IntegrationConnection.

          publishable_key: Your Conductor publishable key, which we use to create the session’s
              `authFlowUrl`.

          link_expiry_mins: The number of minutes after which the AuthSession will expire. Must be at least
              15 minutes and no more than 7 days. If not provided, defaults to 30 minutes.

          redirect_url: The URL to which Conductor will redirect the end-user to return to your app
              after they complete the authentication flow. If not provided, their browser tab
              will close instead.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/auth-sessions",
            body=maybe_transform(
                {
                    "end_user_id": end_user_id,
                    "publishable_key": publishable_key,
                    "link_expiry_mins": link_expiry_mins,
                    "redirect_url": redirect_url,
                },
                auth_session_create_params.AuthSessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthSession,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthSession:
        """
        Retrieves the details of an AuthSession that has previously been created.

        Args:
          id: The ID of the AuthSession to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/auth-sessions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthSession,
        )


class AsyncAuthSessionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuthSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return AsyncAuthSessionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        end_user_id: str,
        publishable_key: str,
        link_expiry_mins: float | NotGiven = NOT_GIVEN,
        redirect_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthSession:
        """
        To launch the authentication flow, create an AuthSession and pass the returned
        session’s `authFlowUrl` to the client for your end-user to visit in their
        browser.

        Args:
          end_user_id: The ID of the EndUser for whom to create the IntegrationConnection.

          publishable_key: Your Conductor publishable key, which we use to create the session’s
              `authFlowUrl`.

          link_expiry_mins: The number of minutes after which the AuthSession will expire. Must be at least
              15 minutes and no more than 7 days. If not provided, defaults to 30 minutes.

          redirect_url: The URL to which Conductor will redirect the end-user to return to your app
              after they complete the authentication flow. If not provided, their browser tab
              will close instead.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/auth-sessions",
            body=await async_maybe_transform(
                {
                    "end_user_id": end_user_id,
                    "publishable_key": publishable_key,
                    "link_expiry_mins": link_expiry_mins,
                    "redirect_url": redirect_url,
                },
                auth_session_create_params.AuthSessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthSession,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthSession:
        """
        Retrieves the details of an AuthSession that has previously been created.

        Args:
          id: The ID of the AuthSession to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/auth-sessions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthSession,
        )


class AuthSessionsResourceWithRawResponse:
    def __init__(self, auth_sessions: AuthSessionsResource) -> None:
        self._auth_sessions = auth_sessions

        self.create = to_raw_response_wrapper(
            auth_sessions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            auth_sessions.retrieve,
        )


class AsyncAuthSessionsResourceWithRawResponse:
    def __init__(self, auth_sessions: AsyncAuthSessionsResource) -> None:
        self._auth_sessions = auth_sessions

        self.create = async_to_raw_response_wrapper(
            auth_sessions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            auth_sessions.retrieve,
        )


class AuthSessionsResourceWithStreamingResponse:
    def __init__(self, auth_sessions: AuthSessionsResource) -> None:
        self._auth_sessions = auth_sessions

        self.create = to_streamed_response_wrapper(
            auth_sessions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            auth_sessions.retrieve,
        )


class AsyncAuthSessionsResourceWithStreamingResponse:
    def __init__(self, auth_sessions: AsyncAuthSessionsResource) -> None:
        self._auth_sessions = auth_sessions

        self.create = async_to_streamed_response_wrapper(
            auth_sessions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            auth_sessions.retrieve,
        )
