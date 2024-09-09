# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .bills import (
    BillsResource,
    AsyncBillsResource,
    BillsResourceWithRawResponse,
    AsyncBillsResourceWithRawResponse,
    BillsResourceWithStreamingResponse,
    AsyncBillsResourceWithStreamingResponse,
)
from .classes import (
    ClassesResource,
    AsyncClassesResource,
    ClassesResourceWithRawResponse,
    AsyncClassesResourceWithRawResponse,
    ClassesResourceWithStreamingResponse,
    AsyncClassesResourceWithStreamingResponse,
)
from .vendors import (
    VendorsResource,
    AsyncVendorsResource,
    VendorsResourceWithRawResponse,
    AsyncVendorsResourceWithRawResponse,
    VendorsResourceWithStreamingResponse,
    AsyncVendorsResourceWithStreamingResponse,
)
from .accounts import (
    AccountsResource,
    AsyncAccountsResource,
    AccountsResourceWithRawResponse,
    AsyncAccountsResourceWithRawResponse,
    AccountsResourceWithStreamingResponse,
    AsyncAccountsResourceWithStreamingResponse,
)
from .invoices import (
    InvoicesResource,
    AsyncInvoicesResource,
    InvoicesResourceWithRawResponse,
    AsyncInvoicesResourceWithRawResponse,
    InvoicesResourceWithStreamingResponse,
    AsyncInvoicesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .customers import (
    CustomersResource,
    AsyncCustomersResource,
    CustomersResourceWithRawResponse,
    AsyncCustomersResourceWithRawResponse,
    CustomersResourceWithStreamingResponse,
    AsyncCustomersResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .standard_terms import (
    StandardTermsResource,
    AsyncStandardTermsResource,
    StandardTermsResourceWithRawResponse,
    AsyncStandardTermsResourceWithRawResponse,
    StandardTermsResourceWithStreamingResponse,
    AsyncStandardTermsResourceWithStreamingResponse,
)
from .credit_card_charges import (
    CreditCardChargesResource,
    AsyncCreditCardChargesResource,
    CreditCardChargesResourceWithRawResponse,
    AsyncCreditCardChargesResourceWithRawResponse,
    CreditCardChargesResourceWithStreamingResponse,
    AsyncCreditCardChargesResourceWithStreamingResponse,
)

__all__ = ["QbdResource", "AsyncQbdResource"]


class QbdResource(SyncAPIResource):
    @cached_property
    def accounts(self) -> AccountsResource:
        return AccountsResource(self._client)

    @cached_property
    def bills(self) -> BillsResource:
        return BillsResource(self._client)

    @cached_property
    def classes(self) -> ClassesResource:
        return ClassesResource(self._client)

    @cached_property
    def credit_card_charges(self) -> CreditCardChargesResource:
        return CreditCardChargesResource(self._client)

    @cached_property
    def customers(self) -> CustomersResource:
        return CustomersResource(self._client)

    @cached_property
    def invoices(self) -> InvoicesResource:
        return InvoicesResource(self._client)

    @cached_property
    def standard_terms(self) -> StandardTermsResource:
        return StandardTermsResource(self._client)

    @cached_property
    def vendors(self) -> VendorsResource:
        return VendorsResource(self._client)

    @cached_property
    def with_raw_response(self) -> QbdResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return QbdResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QbdResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return QbdResourceWithStreamingResponse(self)


class AsyncQbdResource(AsyncAPIResource):
    @cached_property
    def accounts(self) -> AsyncAccountsResource:
        return AsyncAccountsResource(self._client)

    @cached_property
    def bills(self) -> AsyncBillsResource:
        return AsyncBillsResource(self._client)

    @cached_property
    def classes(self) -> AsyncClassesResource:
        return AsyncClassesResource(self._client)

    @cached_property
    def credit_card_charges(self) -> AsyncCreditCardChargesResource:
        return AsyncCreditCardChargesResource(self._client)

    @cached_property
    def customers(self) -> AsyncCustomersResource:
        return AsyncCustomersResource(self._client)

    @cached_property
    def invoices(self) -> AsyncInvoicesResource:
        return AsyncInvoicesResource(self._client)

    @cached_property
    def standard_terms(self) -> AsyncStandardTermsResource:
        return AsyncStandardTermsResource(self._client)

    @cached_property
    def vendors(self) -> AsyncVendorsResource:
        return AsyncVendorsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncQbdResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQbdResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQbdResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return AsyncQbdResourceWithStreamingResponse(self)


class QbdResourceWithRawResponse:
    def __init__(self, qbd: QbdResource) -> None:
        self._qbd = qbd

    @cached_property
    def accounts(self) -> AccountsResourceWithRawResponse:
        return AccountsResourceWithRawResponse(self._qbd.accounts)

    @cached_property
    def bills(self) -> BillsResourceWithRawResponse:
        return BillsResourceWithRawResponse(self._qbd.bills)

    @cached_property
    def classes(self) -> ClassesResourceWithRawResponse:
        return ClassesResourceWithRawResponse(self._qbd.classes)

    @cached_property
    def credit_card_charges(self) -> CreditCardChargesResourceWithRawResponse:
        return CreditCardChargesResourceWithRawResponse(self._qbd.credit_card_charges)

    @cached_property
    def customers(self) -> CustomersResourceWithRawResponse:
        return CustomersResourceWithRawResponse(self._qbd.customers)

    @cached_property
    def invoices(self) -> InvoicesResourceWithRawResponse:
        return InvoicesResourceWithRawResponse(self._qbd.invoices)

    @cached_property
    def standard_terms(self) -> StandardTermsResourceWithRawResponse:
        return StandardTermsResourceWithRawResponse(self._qbd.standard_terms)

    @cached_property
    def vendors(self) -> VendorsResourceWithRawResponse:
        return VendorsResourceWithRawResponse(self._qbd.vendors)


class AsyncQbdResourceWithRawResponse:
    def __init__(self, qbd: AsyncQbdResource) -> None:
        self._qbd = qbd

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithRawResponse:
        return AsyncAccountsResourceWithRawResponse(self._qbd.accounts)

    @cached_property
    def bills(self) -> AsyncBillsResourceWithRawResponse:
        return AsyncBillsResourceWithRawResponse(self._qbd.bills)

    @cached_property
    def classes(self) -> AsyncClassesResourceWithRawResponse:
        return AsyncClassesResourceWithRawResponse(self._qbd.classes)

    @cached_property
    def credit_card_charges(self) -> AsyncCreditCardChargesResourceWithRawResponse:
        return AsyncCreditCardChargesResourceWithRawResponse(self._qbd.credit_card_charges)

    @cached_property
    def customers(self) -> AsyncCustomersResourceWithRawResponse:
        return AsyncCustomersResourceWithRawResponse(self._qbd.customers)

    @cached_property
    def invoices(self) -> AsyncInvoicesResourceWithRawResponse:
        return AsyncInvoicesResourceWithRawResponse(self._qbd.invoices)

    @cached_property
    def standard_terms(self) -> AsyncStandardTermsResourceWithRawResponse:
        return AsyncStandardTermsResourceWithRawResponse(self._qbd.standard_terms)

    @cached_property
    def vendors(self) -> AsyncVendorsResourceWithRawResponse:
        return AsyncVendorsResourceWithRawResponse(self._qbd.vendors)


class QbdResourceWithStreamingResponse:
    def __init__(self, qbd: QbdResource) -> None:
        self._qbd = qbd

    @cached_property
    def accounts(self) -> AccountsResourceWithStreamingResponse:
        return AccountsResourceWithStreamingResponse(self._qbd.accounts)

    @cached_property
    def bills(self) -> BillsResourceWithStreamingResponse:
        return BillsResourceWithStreamingResponse(self._qbd.bills)

    @cached_property
    def classes(self) -> ClassesResourceWithStreamingResponse:
        return ClassesResourceWithStreamingResponse(self._qbd.classes)

    @cached_property
    def credit_card_charges(self) -> CreditCardChargesResourceWithStreamingResponse:
        return CreditCardChargesResourceWithStreamingResponse(self._qbd.credit_card_charges)

    @cached_property
    def customers(self) -> CustomersResourceWithStreamingResponse:
        return CustomersResourceWithStreamingResponse(self._qbd.customers)

    @cached_property
    def invoices(self) -> InvoicesResourceWithStreamingResponse:
        return InvoicesResourceWithStreamingResponse(self._qbd.invoices)

    @cached_property
    def standard_terms(self) -> StandardTermsResourceWithStreamingResponse:
        return StandardTermsResourceWithStreamingResponse(self._qbd.standard_terms)

    @cached_property
    def vendors(self) -> VendorsResourceWithStreamingResponse:
        return VendorsResourceWithStreamingResponse(self._qbd.vendors)


class AsyncQbdResourceWithStreamingResponse:
    def __init__(self, qbd: AsyncQbdResource) -> None:
        self._qbd = qbd

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithStreamingResponse:
        return AsyncAccountsResourceWithStreamingResponse(self._qbd.accounts)

    @cached_property
    def bills(self) -> AsyncBillsResourceWithStreamingResponse:
        return AsyncBillsResourceWithStreamingResponse(self._qbd.bills)

    @cached_property
    def classes(self) -> AsyncClassesResourceWithStreamingResponse:
        return AsyncClassesResourceWithStreamingResponse(self._qbd.classes)

    @cached_property
    def credit_card_charges(self) -> AsyncCreditCardChargesResourceWithStreamingResponse:
        return AsyncCreditCardChargesResourceWithStreamingResponse(self._qbd.credit_card_charges)

    @cached_property
    def customers(self) -> AsyncCustomersResourceWithStreamingResponse:
        return AsyncCustomersResourceWithStreamingResponse(self._qbd.customers)

    @cached_property
    def invoices(self) -> AsyncInvoicesResourceWithStreamingResponse:
        return AsyncInvoicesResourceWithStreamingResponse(self._qbd.invoices)

    @cached_property
    def standard_terms(self) -> AsyncStandardTermsResourceWithStreamingResponse:
        return AsyncStandardTermsResourceWithStreamingResponse(self._qbd.standard_terms)

    @cached_property
    def vendors(self) -> AsyncVendorsResourceWithStreamingResponse:
        return AsyncVendorsResourceWithStreamingResponse(self._qbd.vendors)
