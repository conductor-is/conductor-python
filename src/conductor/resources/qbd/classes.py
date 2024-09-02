# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
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
from ...types.qbd import class_list_params, class_create_params
from ..._base_client import make_request_options
from ...types.qbd.qbd_class import QbdClass
from ...types.qbd.class_list_response import ClassListResponse

__all__ = ["ClassesResource", "AsyncClassesResource"]


class ClassesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClassesResourceWithRawResponse:
        return ClassesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClassesResourceWithStreamingResponse:
        return ClassesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        conductor_end_user_id: str,
        is_active: bool | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QbdClass:
        """Creates a class.

        Args:
          name: The case-insensitive name of the class.

        Does not include the names of its
              accentors like `fullName` does.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          is_active: Whether this class is active. QuickBooks hides inactive objects from most views
              and reports in the UI.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/classes",
            body=maybe_transform(
                {
                    "name": name,
                    "is_active": is_active,
                    "parent_id": parent_id,
                },
                class_create_params.ClassCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QbdClass,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        id: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        full_name: Union[str, List[str]] | NotGiven = NOT_GIVEN,
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
    ) -> ClassListResponse:
        """
        Returns a list of classes.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          id: Filter for classes with the specified QuickBooks-assigned unique identifier(s).
              If your request includes this parameter, all other query parameters will be
              ignored.

          full_name: Filter for classes with this full-name or full-names. Like `id`, a full-name is
              a unique identifier for a class, and is created by prefixing the class's name
              with the names of each ancestor. If your request includes this parameter, all
              other query parameters will be ignored.

          limit: The maximum number of objects to return, ranging from 1 to 500. Defaults to 500.
              NOTE: QuickBooks Desktop does not support cursor-based pagination for this
              endpoint. Hence, this parameter will limit the response size, but you will not
              be able to fetch the next set of results. If you must paginate through the
              results, try iterating via the date-range query parameters.

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
            "/quickbooks-desktop/classes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "full_name": full_name,
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
                    class_list_params.ClassListParams,
                ),
            ),
            cast_to=ClassListResponse,
        )


class AsyncClassesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClassesResourceWithRawResponse:
        return AsyncClassesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClassesResourceWithStreamingResponse:
        return AsyncClassesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        conductor_end_user_id: str,
        is_active: bool | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QbdClass:
        """Creates a class.

        Args:
          name: The case-insensitive name of the class.

        Does not include the names of its
              accentors like `fullName` does.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          is_active: Whether this class is active. QuickBooks hides inactive objects from most views
              and reports in the UI.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/classes",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "is_active": is_active,
                    "parent_id": parent_id,
                },
                class_create_params.ClassCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QbdClass,
        )

    async def list(
        self,
        *,
        conductor_end_user_id: str,
        id: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        full_name: Union[str, List[str]] | NotGiven = NOT_GIVEN,
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
    ) -> ClassListResponse:
        """
        Returns a list of classes.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          id: Filter for classes with the specified QuickBooks-assigned unique identifier(s).
              If your request includes this parameter, all other query parameters will be
              ignored.

          full_name: Filter for classes with this full-name or full-names. Like `id`, a full-name is
              a unique identifier for a class, and is created by prefixing the class's name
              with the names of each ancestor. If your request includes this parameter, all
              other query parameters will be ignored.

          limit: The maximum number of objects to return, ranging from 1 to 500. Defaults to 500.
              NOTE: QuickBooks Desktop does not support cursor-based pagination for this
              endpoint. Hence, this parameter will limit the response size, but you will not
              be able to fetch the next set of results. If you must paginate through the
              results, try iterating via the date-range query parameters.

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
            "/quickbooks-desktop/classes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id": id,
                        "full_name": full_name,
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
                    class_list_params.ClassListParams,
                ),
            ),
            cast_to=ClassListResponse,
        )


class ClassesResourceWithRawResponse:
    def __init__(self, classes: ClassesResource) -> None:
        self._classes = classes

        self.create = to_raw_response_wrapper(
            classes.create,
        )
        self.list = to_raw_response_wrapper(
            classes.list,
        )


class AsyncClassesResourceWithRawResponse:
    def __init__(self, classes: AsyncClassesResource) -> None:
        self._classes = classes

        self.create = async_to_raw_response_wrapper(
            classes.create,
        )
        self.list = async_to_raw_response_wrapper(
            classes.list,
        )


class ClassesResourceWithStreamingResponse:
    def __init__(self, classes: ClassesResource) -> None:
        self._classes = classes

        self.create = to_streamed_response_wrapper(
            classes.create,
        )
        self.list = to_streamed_response_wrapper(
            classes.list,
        )


class AsyncClassesResourceWithStreamingResponse:
    def __init__(self, classes: AsyncClassesResource) -> None:
        self._classes = classes

        self.create = async_to_streamed_response_wrapper(
            classes.create,
        )
        self.list = async_to_streamed_response_wrapper(
            classes.list,
        )
