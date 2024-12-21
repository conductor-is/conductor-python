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
from .checks import (
    ChecksResource,
    AsyncChecksResource,
    ChecksResourceWithRawResponse,
    AsyncChecksResourceWithRawResponse,
    ChecksResourceWithStreamingResponse,
    AsyncChecksResourceWithStreamingResponse,
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
from .estimates import (
    EstimatesResource,
    AsyncEstimatesResource,
    EstimatesResourceWithRawResponse,
    AsyncEstimatesResourceWithRawResponse,
    EstimatesResourceWithStreamingResponse,
    AsyncEstimatesResourceWithStreamingResponse,
)
from .transfers import (
    TransfersResource,
    AsyncTransfersResource,
    TransfersResourceWithRawResponse,
    AsyncTransfersResourceWithRawResponse,
    TransfersResourceWithStreamingResponse,
    AsyncTransfersResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .sales_orders import (
    SalesOrdersResource,
    AsyncSalesOrdersResource,
    SalesOrdersResourceWithRawResponse,
    AsyncSalesOrdersResourceWithRawResponse,
    SalesOrdersResourceWithStreamingResponse,
    AsyncSalesOrdersResourceWithStreamingResponse,
)
from .service_items import (
    ServiceItemsResource,
    AsyncServiceItemsResource,
    ServiceItemsResourceWithRawResponse,
    AsyncServiceItemsResourceWithRawResponse,
    ServiceItemsResourceWithStreamingResponse,
    AsyncServiceItemsResourceWithStreamingResponse,
)
from .sales_receipts import (
    SalesReceiptsResource,
    AsyncSalesReceiptsResource,
    SalesReceiptsResourceWithRawResponse,
    AsyncSalesReceiptsResourceWithRawResponse,
    SalesReceiptsResourceWithStreamingResponse,
    AsyncSalesReceiptsResourceWithStreamingResponse,
)
from .standard_terms import (
    StandardTermsResource,
    AsyncStandardTermsResource,
    StandardTermsResourceWithRawResponse,
    AsyncStandardTermsResourceWithRawResponse,
    StandardTermsResourceWithStreamingResponse,
    AsyncStandardTermsResourceWithStreamingResponse,
)
from .inventory_items import (
    InventoryItemsResource,
    AsyncInventoryItemsResource,
    InventoryItemsResourceWithRawResponse,
    AsyncInventoryItemsResourceWithRawResponse,
    InventoryItemsResourceWithStreamingResponse,
    AsyncInventoryItemsResourceWithStreamingResponse,
)
from .inventory_sites import (
    InventorySitesResource,
    AsyncInventorySitesResource,
    InventorySitesResourceWithRawResponse,
    AsyncInventorySitesResourceWithRawResponse,
    InventorySitesResourceWithStreamingResponse,
    AsyncInventorySitesResourceWithStreamingResponse,
)
from .purchase_orders import (
    PurchaseOrdersResource,
    AsyncPurchaseOrdersResource,
    PurchaseOrdersResourceWithRawResponse,
    AsyncPurchaseOrdersResourceWithRawResponse,
    PurchaseOrdersResourceWithStreamingResponse,
    AsyncPurchaseOrdersResourceWithStreamingResponse,
)
from .sales_tax_codes import (
    SalesTaxCodesResource,
    AsyncSalesTaxCodesResource,
    SalesTaxCodesResourceWithRawResponse,
    AsyncSalesTaxCodesResourceWithRawResponse,
    SalesTaxCodesResourceWithStreamingResponse,
    AsyncSalesTaxCodesResourceWithStreamingResponse,
)
from .sales_tax_items import (
    SalesTaxItemsResource,
    AsyncSalesTaxItemsResource,
    SalesTaxItemsResourceWithRawResponse,
    AsyncSalesTaxItemsResourceWithRawResponse,
    SalesTaxItemsResourceWithStreamingResponse,
    AsyncSalesTaxItemsResourceWithStreamingResponse,
)
from .receive_payments import (
    ReceivePaymentsResource,
    AsyncReceivePaymentsResource,
    ReceivePaymentsResourceWithRawResponse,
    AsyncReceivePaymentsResourceWithRawResponse,
    ReceivePaymentsResourceWithStreamingResponse,
    AsyncReceivePaymentsResourceWithStreamingResponse,
)
from .date_driven_terms import (
    DateDrivenTermsResource,
    AsyncDateDrivenTermsResource,
    DateDrivenTermsResourceWithRawResponse,
    AsyncDateDrivenTermsResourceWithRawResponse,
    DateDrivenTermsResourceWithStreamingResponse,
    AsyncDateDrivenTermsResourceWithStreamingResponse,
)
from .bill_check_payments import (
    BillCheckPaymentsResource,
    AsyncBillCheckPaymentsResource,
    BillCheckPaymentsResourceWithRawResponse,
    AsyncBillCheckPaymentsResourceWithRawResponse,
    BillCheckPaymentsResourceWithStreamingResponse,
    AsyncBillCheckPaymentsResourceWithStreamingResponse,
)
from .credit_card_charges import (
    CreditCardChargesResource,
    AsyncCreditCardChargesResource,
    CreditCardChargesResourceWithRawResponse,
    AsyncCreditCardChargesResourceWithRawResponse,
    CreditCardChargesResourceWithStreamingResponse,
    AsyncCreditCardChargesResourceWithStreamingResponse,
)
from .credit_card_credits import (
    CreditCardCreditsResource,
    AsyncCreditCardCreditsResource,
    CreditCardCreditsResourceWithRawResponse,
    AsyncCreditCardCreditsResourceWithRawResponse,
    CreditCardCreditsResourceWithStreamingResponse,
    AsyncCreditCardCreditsResourceWithStreamingResponse,
)
from .non_inventory_items import (
    NonInventoryItemsResource,
    AsyncNonInventoryItemsResource,
    NonInventoryItemsResourceWithRawResponse,
    AsyncNonInventoryItemsResourceWithRawResponse,
    NonInventoryItemsResourceWithStreamingResponse,
    AsyncNonInventoryItemsResourceWithStreamingResponse,
)
from .inventory_assembly_items import (
    InventoryAssemblyItemsResource,
    AsyncInventoryAssemblyItemsResource,
    InventoryAssemblyItemsResourceWithRawResponse,
    AsyncInventoryAssemblyItemsResourceWithRawResponse,
    InventoryAssemblyItemsResourceWithStreamingResponse,
    AsyncInventoryAssemblyItemsResourceWithStreamingResponse,
)
from .bill_credit_card_payments import (
    BillCreditCardPaymentsResource,
    AsyncBillCreditCardPaymentsResource,
    BillCreditCardPaymentsResourceWithRawResponse,
    AsyncBillCreditCardPaymentsResourceWithRawResponse,
    BillCreditCardPaymentsResourceWithStreamingResponse,
    AsyncBillCreditCardPaymentsResourceWithStreamingResponse,
)

__all__ = ["QbdResource", "AsyncQbdResource"]


class QbdResource(SyncAPIResource):
    @cached_property
    def accounts(self) -> AccountsResource:
        return AccountsResource(self._client)

    @cached_property
    def bill_check_payments(self) -> BillCheckPaymentsResource:
        return BillCheckPaymentsResource(self._client)

    @cached_property
    def bill_credit_card_payments(self) -> BillCreditCardPaymentsResource:
        return BillCreditCardPaymentsResource(self._client)

    @cached_property
    def bills(self) -> BillsResource:
        return BillsResource(self._client)

    @cached_property
    def checks(self) -> ChecksResource:
        return ChecksResource(self._client)

    @cached_property
    def classes(self) -> ClassesResource:
        return ClassesResource(self._client)

    @cached_property
    def credit_card_charges(self) -> CreditCardChargesResource:
        return CreditCardChargesResource(self._client)

    @cached_property
    def credit_card_credits(self) -> CreditCardCreditsResource:
        return CreditCardCreditsResource(self._client)

    @cached_property
    def customers(self) -> CustomersResource:
        return CustomersResource(self._client)

    @cached_property
    def date_driven_terms(self) -> DateDrivenTermsResource:
        return DateDrivenTermsResource(self._client)

    @cached_property
    def estimates(self) -> EstimatesResource:
        return EstimatesResource(self._client)

    @cached_property
    def inventory_assembly_items(self) -> InventoryAssemblyItemsResource:
        return InventoryAssemblyItemsResource(self._client)

    @cached_property
    def inventory_items(self) -> InventoryItemsResource:
        return InventoryItemsResource(self._client)

    @cached_property
    def inventory_sites(self) -> InventorySitesResource:
        return InventorySitesResource(self._client)

    @cached_property
    def invoices(self) -> InvoicesResource:
        return InvoicesResource(self._client)

    @cached_property
    def non_inventory_items(self) -> NonInventoryItemsResource:
        return NonInventoryItemsResource(self._client)

    @cached_property
    def purchase_orders(self) -> PurchaseOrdersResource:
        return PurchaseOrdersResource(self._client)

    @cached_property
    def receive_payments(self) -> ReceivePaymentsResource:
        return ReceivePaymentsResource(self._client)

    @cached_property
    def sales_orders(self) -> SalesOrdersResource:
        return SalesOrdersResource(self._client)

    @cached_property
    def sales_receipts(self) -> SalesReceiptsResource:
        return SalesReceiptsResource(self._client)

    @cached_property
    def sales_tax_codes(self) -> SalesTaxCodesResource:
        return SalesTaxCodesResource(self._client)

    @cached_property
    def sales_tax_items(self) -> SalesTaxItemsResource:
        return SalesTaxItemsResource(self._client)

    @cached_property
    def service_items(self) -> ServiceItemsResource:
        return ServiceItemsResource(self._client)

    @cached_property
    def standard_terms(self) -> StandardTermsResource:
        return StandardTermsResource(self._client)

    @cached_property
    def transfers(self) -> TransfersResource:
        return TransfersResource(self._client)

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
    def bill_check_payments(self) -> AsyncBillCheckPaymentsResource:
        return AsyncBillCheckPaymentsResource(self._client)

    @cached_property
    def bill_credit_card_payments(self) -> AsyncBillCreditCardPaymentsResource:
        return AsyncBillCreditCardPaymentsResource(self._client)

    @cached_property
    def bills(self) -> AsyncBillsResource:
        return AsyncBillsResource(self._client)

    @cached_property
    def checks(self) -> AsyncChecksResource:
        return AsyncChecksResource(self._client)

    @cached_property
    def classes(self) -> AsyncClassesResource:
        return AsyncClassesResource(self._client)

    @cached_property
    def credit_card_charges(self) -> AsyncCreditCardChargesResource:
        return AsyncCreditCardChargesResource(self._client)

    @cached_property
    def credit_card_credits(self) -> AsyncCreditCardCreditsResource:
        return AsyncCreditCardCreditsResource(self._client)

    @cached_property
    def customers(self) -> AsyncCustomersResource:
        return AsyncCustomersResource(self._client)

    @cached_property
    def date_driven_terms(self) -> AsyncDateDrivenTermsResource:
        return AsyncDateDrivenTermsResource(self._client)

    @cached_property
    def estimates(self) -> AsyncEstimatesResource:
        return AsyncEstimatesResource(self._client)

    @cached_property
    def inventory_assembly_items(self) -> AsyncInventoryAssemblyItemsResource:
        return AsyncInventoryAssemblyItemsResource(self._client)

    @cached_property
    def inventory_items(self) -> AsyncInventoryItemsResource:
        return AsyncInventoryItemsResource(self._client)

    @cached_property
    def inventory_sites(self) -> AsyncInventorySitesResource:
        return AsyncInventorySitesResource(self._client)

    @cached_property
    def invoices(self) -> AsyncInvoicesResource:
        return AsyncInvoicesResource(self._client)

    @cached_property
    def non_inventory_items(self) -> AsyncNonInventoryItemsResource:
        return AsyncNonInventoryItemsResource(self._client)

    @cached_property
    def purchase_orders(self) -> AsyncPurchaseOrdersResource:
        return AsyncPurchaseOrdersResource(self._client)

    @cached_property
    def receive_payments(self) -> AsyncReceivePaymentsResource:
        return AsyncReceivePaymentsResource(self._client)

    @cached_property
    def sales_orders(self) -> AsyncSalesOrdersResource:
        return AsyncSalesOrdersResource(self._client)

    @cached_property
    def sales_receipts(self) -> AsyncSalesReceiptsResource:
        return AsyncSalesReceiptsResource(self._client)

    @cached_property
    def sales_tax_codes(self) -> AsyncSalesTaxCodesResource:
        return AsyncSalesTaxCodesResource(self._client)

    @cached_property
    def sales_tax_items(self) -> AsyncSalesTaxItemsResource:
        return AsyncSalesTaxItemsResource(self._client)

    @cached_property
    def service_items(self) -> AsyncServiceItemsResource:
        return AsyncServiceItemsResource(self._client)

    @cached_property
    def standard_terms(self) -> AsyncStandardTermsResource:
        return AsyncStandardTermsResource(self._client)

    @cached_property
    def transfers(self) -> AsyncTransfersResource:
        return AsyncTransfersResource(self._client)

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
    def bill_check_payments(self) -> BillCheckPaymentsResourceWithRawResponse:
        return BillCheckPaymentsResourceWithRawResponse(self._qbd.bill_check_payments)

    @cached_property
    def bill_credit_card_payments(self) -> BillCreditCardPaymentsResourceWithRawResponse:
        return BillCreditCardPaymentsResourceWithRawResponse(self._qbd.bill_credit_card_payments)

    @cached_property
    def bills(self) -> BillsResourceWithRawResponse:
        return BillsResourceWithRawResponse(self._qbd.bills)

    @cached_property
    def checks(self) -> ChecksResourceWithRawResponse:
        return ChecksResourceWithRawResponse(self._qbd.checks)

    @cached_property
    def classes(self) -> ClassesResourceWithRawResponse:
        return ClassesResourceWithRawResponse(self._qbd.classes)

    @cached_property
    def credit_card_charges(self) -> CreditCardChargesResourceWithRawResponse:
        return CreditCardChargesResourceWithRawResponse(self._qbd.credit_card_charges)

    @cached_property
    def credit_card_credits(self) -> CreditCardCreditsResourceWithRawResponse:
        return CreditCardCreditsResourceWithRawResponse(self._qbd.credit_card_credits)

    @cached_property
    def customers(self) -> CustomersResourceWithRawResponse:
        return CustomersResourceWithRawResponse(self._qbd.customers)

    @cached_property
    def date_driven_terms(self) -> DateDrivenTermsResourceWithRawResponse:
        return DateDrivenTermsResourceWithRawResponse(self._qbd.date_driven_terms)

    @cached_property
    def estimates(self) -> EstimatesResourceWithRawResponse:
        return EstimatesResourceWithRawResponse(self._qbd.estimates)

    @cached_property
    def inventory_assembly_items(self) -> InventoryAssemblyItemsResourceWithRawResponse:
        return InventoryAssemblyItemsResourceWithRawResponse(self._qbd.inventory_assembly_items)

    @cached_property
    def inventory_items(self) -> InventoryItemsResourceWithRawResponse:
        return InventoryItemsResourceWithRawResponse(self._qbd.inventory_items)

    @cached_property
    def inventory_sites(self) -> InventorySitesResourceWithRawResponse:
        return InventorySitesResourceWithRawResponse(self._qbd.inventory_sites)

    @cached_property
    def invoices(self) -> InvoicesResourceWithRawResponse:
        return InvoicesResourceWithRawResponse(self._qbd.invoices)

    @cached_property
    def non_inventory_items(self) -> NonInventoryItemsResourceWithRawResponse:
        return NonInventoryItemsResourceWithRawResponse(self._qbd.non_inventory_items)

    @cached_property
    def purchase_orders(self) -> PurchaseOrdersResourceWithRawResponse:
        return PurchaseOrdersResourceWithRawResponse(self._qbd.purchase_orders)

    @cached_property
    def receive_payments(self) -> ReceivePaymentsResourceWithRawResponse:
        return ReceivePaymentsResourceWithRawResponse(self._qbd.receive_payments)

    @cached_property
    def sales_orders(self) -> SalesOrdersResourceWithRawResponse:
        return SalesOrdersResourceWithRawResponse(self._qbd.sales_orders)

    @cached_property
    def sales_receipts(self) -> SalesReceiptsResourceWithRawResponse:
        return SalesReceiptsResourceWithRawResponse(self._qbd.sales_receipts)

    @cached_property
    def sales_tax_codes(self) -> SalesTaxCodesResourceWithRawResponse:
        return SalesTaxCodesResourceWithRawResponse(self._qbd.sales_tax_codes)

    @cached_property
    def sales_tax_items(self) -> SalesTaxItemsResourceWithRawResponse:
        return SalesTaxItemsResourceWithRawResponse(self._qbd.sales_tax_items)

    @cached_property
    def service_items(self) -> ServiceItemsResourceWithRawResponse:
        return ServiceItemsResourceWithRawResponse(self._qbd.service_items)

    @cached_property
    def standard_terms(self) -> StandardTermsResourceWithRawResponse:
        return StandardTermsResourceWithRawResponse(self._qbd.standard_terms)

    @cached_property
    def transfers(self) -> TransfersResourceWithRawResponse:
        return TransfersResourceWithRawResponse(self._qbd.transfers)

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
    def bill_check_payments(self) -> AsyncBillCheckPaymentsResourceWithRawResponse:
        return AsyncBillCheckPaymentsResourceWithRawResponse(self._qbd.bill_check_payments)

    @cached_property
    def bill_credit_card_payments(self) -> AsyncBillCreditCardPaymentsResourceWithRawResponse:
        return AsyncBillCreditCardPaymentsResourceWithRawResponse(self._qbd.bill_credit_card_payments)

    @cached_property
    def bills(self) -> AsyncBillsResourceWithRawResponse:
        return AsyncBillsResourceWithRawResponse(self._qbd.bills)

    @cached_property
    def checks(self) -> AsyncChecksResourceWithRawResponse:
        return AsyncChecksResourceWithRawResponse(self._qbd.checks)

    @cached_property
    def classes(self) -> AsyncClassesResourceWithRawResponse:
        return AsyncClassesResourceWithRawResponse(self._qbd.classes)

    @cached_property
    def credit_card_charges(self) -> AsyncCreditCardChargesResourceWithRawResponse:
        return AsyncCreditCardChargesResourceWithRawResponse(self._qbd.credit_card_charges)

    @cached_property
    def credit_card_credits(self) -> AsyncCreditCardCreditsResourceWithRawResponse:
        return AsyncCreditCardCreditsResourceWithRawResponse(self._qbd.credit_card_credits)

    @cached_property
    def customers(self) -> AsyncCustomersResourceWithRawResponse:
        return AsyncCustomersResourceWithRawResponse(self._qbd.customers)

    @cached_property
    def date_driven_terms(self) -> AsyncDateDrivenTermsResourceWithRawResponse:
        return AsyncDateDrivenTermsResourceWithRawResponse(self._qbd.date_driven_terms)

    @cached_property
    def estimates(self) -> AsyncEstimatesResourceWithRawResponse:
        return AsyncEstimatesResourceWithRawResponse(self._qbd.estimates)

    @cached_property
    def inventory_assembly_items(self) -> AsyncInventoryAssemblyItemsResourceWithRawResponse:
        return AsyncInventoryAssemblyItemsResourceWithRawResponse(self._qbd.inventory_assembly_items)

    @cached_property
    def inventory_items(self) -> AsyncInventoryItemsResourceWithRawResponse:
        return AsyncInventoryItemsResourceWithRawResponse(self._qbd.inventory_items)

    @cached_property
    def inventory_sites(self) -> AsyncInventorySitesResourceWithRawResponse:
        return AsyncInventorySitesResourceWithRawResponse(self._qbd.inventory_sites)

    @cached_property
    def invoices(self) -> AsyncInvoicesResourceWithRawResponse:
        return AsyncInvoicesResourceWithRawResponse(self._qbd.invoices)

    @cached_property
    def non_inventory_items(self) -> AsyncNonInventoryItemsResourceWithRawResponse:
        return AsyncNonInventoryItemsResourceWithRawResponse(self._qbd.non_inventory_items)

    @cached_property
    def purchase_orders(self) -> AsyncPurchaseOrdersResourceWithRawResponse:
        return AsyncPurchaseOrdersResourceWithRawResponse(self._qbd.purchase_orders)

    @cached_property
    def receive_payments(self) -> AsyncReceivePaymentsResourceWithRawResponse:
        return AsyncReceivePaymentsResourceWithRawResponse(self._qbd.receive_payments)

    @cached_property
    def sales_orders(self) -> AsyncSalesOrdersResourceWithRawResponse:
        return AsyncSalesOrdersResourceWithRawResponse(self._qbd.sales_orders)

    @cached_property
    def sales_receipts(self) -> AsyncSalesReceiptsResourceWithRawResponse:
        return AsyncSalesReceiptsResourceWithRawResponse(self._qbd.sales_receipts)

    @cached_property
    def sales_tax_codes(self) -> AsyncSalesTaxCodesResourceWithRawResponse:
        return AsyncSalesTaxCodesResourceWithRawResponse(self._qbd.sales_tax_codes)

    @cached_property
    def sales_tax_items(self) -> AsyncSalesTaxItemsResourceWithRawResponse:
        return AsyncSalesTaxItemsResourceWithRawResponse(self._qbd.sales_tax_items)

    @cached_property
    def service_items(self) -> AsyncServiceItemsResourceWithRawResponse:
        return AsyncServiceItemsResourceWithRawResponse(self._qbd.service_items)

    @cached_property
    def standard_terms(self) -> AsyncStandardTermsResourceWithRawResponse:
        return AsyncStandardTermsResourceWithRawResponse(self._qbd.standard_terms)

    @cached_property
    def transfers(self) -> AsyncTransfersResourceWithRawResponse:
        return AsyncTransfersResourceWithRawResponse(self._qbd.transfers)

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
    def bill_check_payments(self) -> BillCheckPaymentsResourceWithStreamingResponse:
        return BillCheckPaymentsResourceWithStreamingResponse(self._qbd.bill_check_payments)

    @cached_property
    def bill_credit_card_payments(self) -> BillCreditCardPaymentsResourceWithStreamingResponse:
        return BillCreditCardPaymentsResourceWithStreamingResponse(self._qbd.bill_credit_card_payments)

    @cached_property
    def bills(self) -> BillsResourceWithStreamingResponse:
        return BillsResourceWithStreamingResponse(self._qbd.bills)

    @cached_property
    def checks(self) -> ChecksResourceWithStreamingResponse:
        return ChecksResourceWithStreamingResponse(self._qbd.checks)

    @cached_property
    def classes(self) -> ClassesResourceWithStreamingResponse:
        return ClassesResourceWithStreamingResponse(self._qbd.classes)

    @cached_property
    def credit_card_charges(self) -> CreditCardChargesResourceWithStreamingResponse:
        return CreditCardChargesResourceWithStreamingResponse(self._qbd.credit_card_charges)

    @cached_property
    def credit_card_credits(self) -> CreditCardCreditsResourceWithStreamingResponse:
        return CreditCardCreditsResourceWithStreamingResponse(self._qbd.credit_card_credits)

    @cached_property
    def customers(self) -> CustomersResourceWithStreamingResponse:
        return CustomersResourceWithStreamingResponse(self._qbd.customers)

    @cached_property
    def date_driven_terms(self) -> DateDrivenTermsResourceWithStreamingResponse:
        return DateDrivenTermsResourceWithStreamingResponse(self._qbd.date_driven_terms)

    @cached_property
    def estimates(self) -> EstimatesResourceWithStreamingResponse:
        return EstimatesResourceWithStreamingResponse(self._qbd.estimates)

    @cached_property
    def inventory_assembly_items(self) -> InventoryAssemblyItemsResourceWithStreamingResponse:
        return InventoryAssemblyItemsResourceWithStreamingResponse(self._qbd.inventory_assembly_items)

    @cached_property
    def inventory_items(self) -> InventoryItemsResourceWithStreamingResponse:
        return InventoryItemsResourceWithStreamingResponse(self._qbd.inventory_items)

    @cached_property
    def inventory_sites(self) -> InventorySitesResourceWithStreamingResponse:
        return InventorySitesResourceWithStreamingResponse(self._qbd.inventory_sites)

    @cached_property
    def invoices(self) -> InvoicesResourceWithStreamingResponse:
        return InvoicesResourceWithStreamingResponse(self._qbd.invoices)

    @cached_property
    def non_inventory_items(self) -> NonInventoryItemsResourceWithStreamingResponse:
        return NonInventoryItemsResourceWithStreamingResponse(self._qbd.non_inventory_items)

    @cached_property
    def purchase_orders(self) -> PurchaseOrdersResourceWithStreamingResponse:
        return PurchaseOrdersResourceWithStreamingResponse(self._qbd.purchase_orders)

    @cached_property
    def receive_payments(self) -> ReceivePaymentsResourceWithStreamingResponse:
        return ReceivePaymentsResourceWithStreamingResponse(self._qbd.receive_payments)

    @cached_property
    def sales_orders(self) -> SalesOrdersResourceWithStreamingResponse:
        return SalesOrdersResourceWithStreamingResponse(self._qbd.sales_orders)

    @cached_property
    def sales_receipts(self) -> SalesReceiptsResourceWithStreamingResponse:
        return SalesReceiptsResourceWithStreamingResponse(self._qbd.sales_receipts)

    @cached_property
    def sales_tax_codes(self) -> SalesTaxCodesResourceWithStreamingResponse:
        return SalesTaxCodesResourceWithStreamingResponse(self._qbd.sales_tax_codes)

    @cached_property
    def sales_tax_items(self) -> SalesTaxItemsResourceWithStreamingResponse:
        return SalesTaxItemsResourceWithStreamingResponse(self._qbd.sales_tax_items)

    @cached_property
    def service_items(self) -> ServiceItemsResourceWithStreamingResponse:
        return ServiceItemsResourceWithStreamingResponse(self._qbd.service_items)

    @cached_property
    def standard_terms(self) -> StandardTermsResourceWithStreamingResponse:
        return StandardTermsResourceWithStreamingResponse(self._qbd.standard_terms)

    @cached_property
    def transfers(self) -> TransfersResourceWithStreamingResponse:
        return TransfersResourceWithStreamingResponse(self._qbd.transfers)

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
    def bill_check_payments(self) -> AsyncBillCheckPaymentsResourceWithStreamingResponse:
        return AsyncBillCheckPaymentsResourceWithStreamingResponse(self._qbd.bill_check_payments)

    @cached_property
    def bill_credit_card_payments(self) -> AsyncBillCreditCardPaymentsResourceWithStreamingResponse:
        return AsyncBillCreditCardPaymentsResourceWithStreamingResponse(self._qbd.bill_credit_card_payments)

    @cached_property
    def bills(self) -> AsyncBillsResourceWithStreamingResponse:
        return AsyncBillsResourceWithStreamingResponse(self._qbd.bills)

    @cached_property
    def checks(self) -> AsyncChecksResourceWithStreamingResponse:
        return AsyncChecksResourceWithStreamingResponse(self._qbd.checks)

    @cached_property
    def classes(self) -> AsyncClassesResourceWithStreamingResponse:
        return AsyncClassesResourceWithStreamingResponse(self._qbd.classes)

    @cached_property
    def credit_card_charges(self) -> AsyncCreditCardChargesResourceWithStreamingResponse:
        return AsyncCreditCardChargesResourceWithStreamingResponse(self._qbd.credit_card_charges)

    @cached_property
    def credit_card_credits(self) -> AsyncCreditCardCreditsResourceWithStreamingResponse:
        return AsyncCreditCardCreditsResourceWithStreamingResponse(self._qbd.credit_card_credits)

    @cached_property
    def customers(self) -> AsyncCustomersResourceWithStreamingResponse:
        return AsyncCustomersResourceWithStreamingResponse(self._qbd.customers)

    @cached_property
    def date_driven_terms(self) -> AsyncDateDrivenTermsResourceWithStreamingResponse:
        return AsyncDateDrivenTermsResourceWithStreamingResponse(self._qbd.date_driven_terms)

    @cached_property
    def estimates(self) -> AsyncEstimatesResourceWithStreamingResponse:
        return AsyncEstimatesResourceWithStreamingResponse(self._qbd.estimates)

    @cached_property
    def inventory_assembly_items(self) -> AsyncInventoryAssemblyItemsResourceWithStreamingResponse:
        return AsyncInventoryAssemblyItemsResourceWithStreamingResponse(self._qbd.inventory_assembly_items)

    @cached_property
    def inventory_items(self) -> AsyncInventoryItemsResourceWithStreamingResponse:
        return AsyncInventoryItemsResourceWithStreamingResponse(self._qbd.inventory_items)

    @cached_property
    def inventory_sites(self) -> AsyncInventorySitesResourceWithStreamingResponse:
        return AsyncInventorySitesResourceWithStreamingResponse(self._qbd.inventory_sites)

    @cached_property
    def invoices(self) -> AsyncInvoicesResourceWithStreamingResponse:
        return AsyncInvoicesResourceWithStreamingResponse(self._qbd.invoices)

    @cached_property
    def non_inventory_items(self) -> AsyncNonInventoryItemsResourceWithStreamingResponse:
        return AsyncNonInventoryItemsResourceWithStreamingResponse(self._qbd.non_inventory_items)

    @cached_property
    def purchase_orders(self) -> AsyncPurchaseOrdersResourceWithStreamingResponse:
        return AsyncPurchaseOrdersResourceWithStreamingResponse(self._qbd.purchase_orders)

    @cached_property
    def receive_payments(self) -> AsyncReceivePaymentsResourceWithStreamingResponse:
        return AsyncReceivePaymentsResourceWithStreamingResponse(self._qbd.receive_payments)

    @cached_property
    def sales_orders(self) -> AsyncSalesOrdersResourceWithStreamingResponse:
        return AsyncSalesOrdersResourceWithStreamingResponse(self._qbd.sales_orders)

    @cached_property
    def sales_receipts(self) -> AsyncSalesReceiptsResourceWithStreamingResponse:
        return AsyncSalesReceiptsResourceWithStreamingResponse(self._qbd.sales_receipts)

    @cached_property
    def sales_tax_codes(self) -> AsyncSalesTaxCodesResourceWithStreamingResponse:
        return AsyncSalesTaxCodesResourceWithStreamingResponse(self._qbd.sales_tax_codes)

    @cached_property
    def sales_tax_items(self) -> AsyncSalesTaxItemsResourceWithStreamingResponse:
        return AsyncSalesTaxItemsResourceWithStreamingResponse(self._qbd.sales_tax_items)

    @cached_property
    def service_items(self) -> AsyncServiceItemsResourceWithStreamingResponse:
        return AsyncServiceItemsResourceWithStreamingResponse(self._qbd.service_items)

    @cached_property
    def standard_terms(self) -> AsyncStandardTermsResourceWithStreamingResponse:
        return AsyncStandardTermsResourceWithStreamingResponse(self._qbd.standard_terms)

    @cached_property
    def transfers(self) -> AsyncTransfersResourceWithStreamingResponse:
        return AsyncTransfersResourceWithStreamingResponse(self._qbd.transfers)

    @cached_property
    def vendors(self) -> AsyncVendorsResourceWithStreamingResponse:
        return AsyncVendorsResourceWithStreamingResponse(self._qbd.vendors)
