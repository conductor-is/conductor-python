# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.qbd import standard_term_list_params, standard_term_create_params
from ..._base_client import make_request_options
from ...types.qbd.qbd_standard_term import QbdStandardTerm
from ...types.qbd.standard_term_list_response import StandardTermListResponse

__all__ = ["StandardTermsResource", "AsyncStandardTermsResource"]


class StandardTermsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StandardTermsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return StandardTermsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StandardTermsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return StandardTermsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        conductor_end_user_id: str,
        discount_days: float | NotGiven = NOT_GIVEN,
        discount_percentage: str | NotGiven = NOT_GIVEN,
        due_days: float | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QbdStandardTerm:
        """
        Creates a standard term.

        Args:
          name: The case-insensitive unique name of this standard term, unique across all
              standard terms.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          discount_days: The number of days within which payment must be received to qualify for the
              discount specified by `discountPercentage`.

          discount_percentage: The discount percentage applied to the payment if received within the number of
              days specified by `discountDays`. The value is between 0 and 100.

          due_days: The number of days until payment is due.

          is_active: Indicates whether this standard term is active. Inactive objects are typically
              hidden from views and reports in QuickBooks.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/standard-terms",
            body=maybe_transform(
                {
                    "name": name,
                    "discount_days": discount_days,
                    "discount_percentage": discount_percentage,
                    "due_days": due_days,
                    "is_active": is_active,
                },
                standard_term_create_params.StandardTermCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QbdStandardTerm,
        )

    def retrieve(
        self,
        id: str,
        *,
        conductor_end_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QbdStandardTerm:
        """
        Retrieves a standard term by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the standard term to retrieve.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get(
            f"/quickbooks-desktop/standard-terms/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QbdStandardTerm,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        full_names: str | NotGiven = NOT_GIVEN,
        ids: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name_contains: str | NotGiven = NOT_GIVEN,
        name_ends_with: str | NotGiven = NOT_GIVEN,
        name_from: str | NotGiven = NOT_GIVEN,
        name_starts_with: str | NotGiven = NOT_GIVEN,
        name_to: str | NotGiven = NOT_GIVEN,
        status: Literal["active", "all", "inactive"] | NotGiven = NOT_GIVEN,
        updated_after: str | NotGiven = NOT_GIVEN,
        updated_before: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StandardTermListResponse:
        """
        Returns a list of standard terms.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          full_names: Filter for specific standard terms by their full-name(s). Specify a single
              full-name or multiple using a comma-separated list (e.g., `fullNames=1,2,3`).
              Like `id`, a `fullName` is a unique identifier for a standard term, and is
              formed by by combining the names of its parent objects with its own `name`,
              separated by colons. For example, if a standard term is under "Payment Terms"
              and has the `name` "Net 15", its `fullName` would be "Payment Terms:Net 15".
              Unlike `name`, `fullName` is guaranteed to be unique across all standard term
              objects. Not case-sensitive. NOTE: If you include this parameter, all other
              query parameters will be ignored.

          ids: Filter for specific standard terms by their QuickBooks-assigned unique
              identifier(s). Specify a single ID or multiple using a comma-separated list
              (e.g., `ids=1,2,3`). NOTE: If you include this parameter, all other query
              parameters will be ignored.

          limit: The maximum number of objects to return, ranging from 1 to 500. Defaults to 500.
              NOTE: QuickBooks Desktop does not support cursor-based pagination for this
              object type. Hence, this parameter will limit the response size, but you will
              not be able to fetch the next set of results. To paginate through the results
              for this endpoint, try fetching batches via the date-range query parameters.

          name_contains: Filter for objects whose `name` contains this substring. If you use this
              parameter, you cannot use `nameStartsWith` or `nameEndsWith`.

          name_ends_with: Filter for objects whose `name` ends with this substring. If you use this
              parameter, you cannot use `nameContains` or `nameStartsWith`.

          name_from: Filter for objects whose `name` is alphabetically greater than or equal to this
              value.

          name_starts_with: Filter for objects whose `name` starts with this substring. If you use this
              parameter, you cannot use `nameContains` or `nameEndsWith`.

          name_to: Filter for objects whose `name` is alphabetically less than or equal to this
              value.

          status: Filter for objects that are active, inactive, or both.

          updated_after: Filter for objects updated on or after this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 00:00:00 of that day.

          updated_before: Filter for objects updated on or before this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get(
            "/quickbooks-desktop/standard-terms",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "full_names": full_names,
                        "ids": ids,
                        "limit": limit,
                        "name_contains": name_contains,
                        "name_ends_with": name_ends_with,
                        "name_from": name_from,
                        "name_starts_with": name_starts_with,
                        "name_to": name_to,
                        "status": status,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    standard_term_list_params.StandardTermListParams,
                ),
            ),
            cast_to=StandardTermListResponse,
        )


class AsyncStandardTermsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStandardTermsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStandardTermsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStandardTermsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return AsyncStandardTermsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        conductor_end_user_id: str,
        discount_days: float | NotGiven = NOT_GIVEN,
        discount_percentage: str | NotGiven = NOT_GIVEN,
        due_days: float | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QbdStandardTerm:
        """
        Creates a standard term.

        Args:
          name: The case-insensitive unique name of this standard term, unique across all
              standard terms.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          discount_days: The number of days within which payment must be received to qualify for the
              discount specified by `discountPercentage`.

          discount_percentage: The discount percentage applied to the payment if received within the number of
              days specified by `discountDays`. The value is between 0 and 100.

          due_days: The number of days until payment is due.

          is_active: Indicates whether this standard term is active. Inactive objects are typically
              hidden from views and reports in QuickBooks.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/standard-terms",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "discount_days": discount_days,
                    "discount_percentage": discount_percentage,
                    "due_days": due_days,
                    "is_active": is_active,
                },
                standard_term_create_params.StandardTermCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QbdStandardTerm,
        )

    async def retrieve(
        self,
        id: str,
        *,
        conductor_end_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QbdStandardTerm:
        """
        Retrieves a standard term by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the standard term to retrieve.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._get(
            f"/quickbooks-desktop/standard-terms/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QbdStandardTerm,
        )

    async def list(
        self,
        *,
        conductor_end_user_id: str,
        full_names: str | NotGiven = NOT_GIVEN,
        ids: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name_contains: str | NotGiven = NOT_GIVEN,
        name_ends_with: str | NotGiven = NOT_GIVEN,
        name_from: str | NotGiven = NOT_GIVEN,
        name_starts_with: str | NotGiven = NOT_GIVEN,
        name_to: str | NotGiven = NOT_GIVEN,
        status: Literal["active", "all", "inactive"] | NotGiven = NOT_GIVEN,
        updated_after: str | NotGiven = NOT_GIVEN,
        updated_before: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StandardTermListResponse:
        """
        Returns a list of standard terms.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          full_names: Filter for specific standard terms by their full-name(s). Specify a single
              full-name or multiple using a comma-separated list (e.g., `fullNames=1,2,3`).
              Like `id`, a `fullName` is a unique identifier for a standard term, and is
              formed by by combining the names of its parent objects with its own `name`,
              separated by colons. For example, if a standard term is under "Payment Terms"
              and has the `name` "Net 15", its `fullName` would be "Payment Terms:Net 15".
              Unlike `name`, `fullName` is guaranteed to be unique across all standard term
              objects. Not case-sensitive. NOTE: If you include this parameter, all other
              query parameters will be ignored.

          ids: Filter for specific standard terms by their QuickBooks-assigned unique
              identifier(s). Specify a single ID or multiple using a comma-separated list
              (e.g., `ids=1,2,3`). NOTE: If you include this parameter, all other query
              parameters will be ignored.

          limit: The maximum number of objects to return, ranging from 1 to 500. Defaults to 500.
              NOTE: QuickBooks Desktop does not support cursor-based pagination for this
              object type. Hence, this parameter will limit the response size, but you will
              not be able to fetch the next set of results. To paginate through the results
              for this endpoint, try fetching batches via the date-range query parameters.

          name_contains: Filter for objects whose `name` contains this substring. If you use this
              parameter, you cannot use `nameStartsWith` or `nameEndsWith`.

          name_ends_with: Filter for objects whose `name` ends with this substring. If you use this
              parameter, you cannot use `nameContains` or `nameStartsWith`.

          name_from: Filter for objects whose `name` is alphabetically greater than or equal to this
              value.

          name_starts_with: Filter for objects whose `name` starts with this substring. If you use this
              parameter, you cannot use `nameContains` or `nameEndsWith`.

          name_to: Filter for objects whose `name` is alphabetically less than or equal to this
              value.

          status: Filter for objects that are active, inactive, or both.

          updated_after: Filter for objects updated on or after this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 00:00:00 of that day.

          updated_before: Filter for objects updated on or before this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._get(
            "/quickbooks-desktop/standard-terms",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "full_names": full_names,
                        "ids": ids,
                        "limit": limit,
                        "name_contains": name_contains,
                        "name_ends_with": name_ends_with,
                        "name_from": name_from,
                        "name_starts_with": name_starts_with,
                        "name_to": name_to,
                        "status": status,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    standard_term_list_params.StandardTermListParams,
                ),
            ),
            cast_to=StandardTermListResponse,
        )


class StandardTermsResourceWithRawResponse:
    def __init__(self, standard_terms: StandardTermsResource) -> None:
        self._standard_terms = standard_terms

        self.create = to_raw_response_wrapper(
            standard_terms.create,
        )
        self.retrieve = to_raw_response_wrapper(
            standard_terms.retrieve,
        )
        self.list = to_raw_response_wrapper(
            standard_terms.list,
        )


class AsyncStandardTermsResourceWithRawResponse:
    def __init__(self, standard_terms: AsyncStandardTermsResource) -> None:
        self._standard_terms = standard_terms

        self.create = async_to_raw_response_wrapper(
            standard_terms.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            standard_terms.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            standard_terms.list,
        )


class StandardTermsResourceWithStreamingResponse:
    def __init__(self, standard_terms: StandardTermsResource) -> None:
        self._standard_terms = standard_terms

        self.create = to_streamed_response_wrapper(
            standard_terms.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            standard_terms.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            standard_terms.list,
        )


class AsyncStandardTermsResourceWithStreamingResponse:
    def __init__(self, standard_terms: AsyncStandardTermsResource) -> None:
        self._standard_terms = standard_terms

        self.create = async_to_streamed_response_wrapper(
            standard_terms.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            standard_terms.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            standard_terms.list,
        )
