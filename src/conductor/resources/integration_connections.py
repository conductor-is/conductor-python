# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.integration_connection import IntegrationConnection
from ..types.integration_connection_list_response import IntegrationConnectionListResponse

__all__ = ["IntegrationConnectionsResource", "AsyncIntegrationConnectionsResource"]


class IntegrationConnectionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IntegrationConnectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return IntegrationConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IntegrationConnectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return IntegrationConnectionsResourceWithStreamingResponse(self)

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
    ) -> IntegrationConnection:
        """
        Retrieves an IntegrationConnection object.

        Args:
          id: The ID of the IntegrationConnection to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/integration-connections/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationConnection,
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
    ) -> IntegrationConnectionListResponse:
        """Returns a list of all IntegrationConnections belonging to all of your EndUsers."""
        return self._get(
            "/integration-connections",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationConnectionListResponse,
        )


class AsyncIntegrationConnectionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIntegrationConnectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIntegrationConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIntegrationConnectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return AsyncIntegrationConnectionsResourceWithStreamingResponse(self)

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
    ) -> IntegrationConnection:
        """
        Retrieves an IntegrationConnection object.

        Args:
          id: The ID of the IntegrationConnection to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/integration-connections/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationConnection,
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
    ) -> IntegrationConnectionListResponse:
        """Returns a list of all IntegrationConnections belonging to all of your EndUsers."""
        return await self._get(
            "/integration-connections",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationConnectionListResponse,
        )


class IntegrationConnectionsResourceWithRawResponse:
    def __init__(self, integration_connections: IntegrationConnectionsResource) -> None:
        self._integration_connections = integration_connections

        self.retrieve = to_raw_response_wrapper(
            integration_connections.retrieve,
        )
        self.list = to_raw_response_wrapper(
            integration_connections.list,
        )


class AsyncIntegrationConnectionsResourceWithRawResponse:
    def __init__(self, integration_connections: AsyncIntegrationConnectionsResource) -> None:
        self._integration_connections = integration_connections

        self.retrieve = async_to_raw_response_wrapper(
            integration_connections.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            integration_connections.list,
        )


class IntegrationConnectionsResourceWithStreamingResponse:
    def __init__(self, integration_connections: IntegrationConnectionsResource) -> None:
        self._integration_connections = integration_connections

        self.retrieve = to_streamed_response_wrapper(
            integration_connections.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            integration_connections.list,
        )


class AsyncIntegrationConnectionsResourceWithStreamingResponse:
    def __init__(self, integration_connections: AsyncIntegrationConnectionsResource) -> None:
        self._integration_connections = integration_connections

        self.retrieve = async_to_streamed_response_wrapper(
            integration_connections.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            integration_connections.list,
        )
