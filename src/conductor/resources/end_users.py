# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import end_user_create_params, end_user_request_params
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
from ..types.end_user import EndUser
from ..types.end_user_list_response import EndUserListResponse
from ..types.end_user_ping_response import EndUserPingResponse

__all__ = ["EndUsersResource", "AsyncEndUsersResource"]


class EndUsersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EndUsersResourceWithRawResponse:
        return EndUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EndUsersResourceWithStreamingResponse:
        return EndUsersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        company_name: str,
        email: str,
        source_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EndUser:
        """
        Creates an EndUser.

        Args:
          company_name: Your end-user's company name that will be shown elsewhere in Conductor.

          email: Your end-user's email address for identification purposes. Setting this field
              will not cause any emails to be sent.

          source_id: A unique identifier for your end-user from your system. Maps users between your
              database and Conductor. Must be unique for each user. If you have only one user,
              you may use any string value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/end-users",
            body=maybe_transform(
                {
                    "company_name": company_name,
                    "email": email,
                    "source_id": source_id,
                },
                end_user_create_params.EndUserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EndUser,
        )

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EndUser:
        """Retrieves an EndUser object."""
        return self._get(
            "/end-users/:id",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EndUser,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EndUserListResponse:
        """Returns a list of your EndUsers."""
        return self._get(
            "/end-users",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EndUserListResponse,
        )

    def ping(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EndUserPingResponse:
        """
        Checks whether the specified IntegrationConnection can connect and process
        requests end-to-end. This is useful for showing a "connection status" indicator
        in your app.
        """
        return self._get(
            "/end-users/:id/ping/:integrationSlug",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EndUserPingResponse,
        )

    def request(
        self,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Sends a request to the specified integration connection (e.g.

        QuickBooks
        Desktop) on behalf of the end-user.

        Args:
          body: The request body to send to the integration connection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/end-users/:id/request/:integrationSlug",
            body=maybe_transform(body, end_user_request_params.EndUserRequestParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncEndUsersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEndUsersResourceWithRawResponse:
        return AsyncEndUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEndUsersResourceWithStreamingResponse:
        return AsyncEndUsersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        company_name: str,
        email: str,
        source_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EndUser:
        """
        Creates an EndUser.

        Args:
          company_name: Your end-user's company name that will be shown elsewhere in Conductor.

          email: Your end-user's email address for identification purposes. Setting this field
              will not cause any emails to be sent.

          source_id: A unique identifier for your end-user from your system. Maps users between your
              database and Conductor. Must be unique for each user. If you have only one user,
              you may use any string value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/end-users",
            body=await async_maybe_transform(
                {
                    "company_name": company_name,
                    "email": email,
                    "source_id": source_id,
                },
                end_user_create_params.EndUserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EndUser,
        )

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EndUser:
        """Retrieves an EndUser object."""
        return await self._get(
            "/end-users/:id",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EndUser,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EndUserListResponse:
        """Returns a list of your EndUsers."""
        return await self._get(
            "/end-users",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EndUserListResponse,
        )

    async def ping(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EndUserPingResponse:
        """
        Checks whether the specified IntegrationConnection can connect and process
        requests end-to-end. This is useful for showing a "connection status" indicator
        in your app.
        """
        return await self._get(
            "/end-users/:id/ping/:integrationSlug",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EndUserPingResponse,
        )

    async def request(
        self,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Sends a request to the specified integration connection (e.g.

        QuickBooks
        Desktop) on behalf of the end-user.

        Args:
          body: The request body to send to the integration connection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/end-users/:id/request/:integrationSlug",
            body=await async_maybe_transform(body, end_user_request_params.EndUserRequestParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class EndUsersResourceWithRawResponse:
    def __init__(self, end_users: EndUsersResource) -> None:
        self._end_users = end_users

        self.create = to_raw_response_wrapper(
            end_users.create,
        )
        self.retrieve = to_raw_response_wrapper(
            end_users.retrieve,
        )
        self.list = to_raw_response_wrapper(
            end_users.list,
        )
        self.ping = to_raw_response_wrapper(
            end_users.ping,
        )
        self.request = to_raw_response_wrapper(
            end_users.request,
        )


class AsyncEndUsersResourceWithRawResponse:
    def __init__(self, end_users: AsyncEndUsersResource) -> None:
        self._end_users = end_users

        self.create = async_to_raw_response_wrapper(
            end_users.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            end_users.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            end_users.list,
        )
        self.ping = async_to_raw_response_wrapper(
            end_users.ping,
        )
        self.request = async_to_raw_response_wrapper(
            end_users.request,
        )


class EndUsersResourceWithStreamingResponse:
    def __init__(self, end_users: EndUsersResource) -> None:
        self._end_users = end_users

        self.create = to_streamed_response_wrapper(
            end_users.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            end_users.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            end_users.list,
        )
        self.ping = to_streamed_response_wrapper(
            end_users.ping,
        )
        self.request = to_streamed_response_wrapper(
            end_users.request,
        )


class AsyncEndUsersResourceWithStreamingResponse:
    def __init__(self, end_users: AsyncEndUsersResource) -> None:
        self._end_users = end_users

        self.create = async_to_streamed_response_wrapper(
            end_users.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            end_users.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            end_users.list,
        )
        self.ping = async_to_streamed_response_wrapper(
            end_users.ping,
        )
        self.request = async_to_streamed_response_wrapper(
            end_users.request,
        )
