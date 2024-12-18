# AuthSessions

Types:

```python
from conductor.types import AuthSession
```

Methods:

- <code title="post /auth-sessions">client.auth_sessions.<a href="./src/conductor/resources/auth_sessions.py">create</a>(\*\*<a href="src/conductor/types/auth_session_create_params.py">params</a>) -> <a href="./src/conductor/types/auth_session.py">AuthSession</a></code>
- <code title="get /auth-sessions/{id}">client.auth_sessions.<a href="./src/conductor/resources/auth_sessions.py">retrieve</a>(id) -> <a href="./src/conductor/types/auth_session.py">AuthSession</a></code>

# EndUsers

Types:

```python
from conductor.types import (
    EndUser,
    EndUserListResponse,
    EndUserDeleteResponse,
    EndUserPassthroughIntegrationResponse,
    EndUserPingResponse,
)
```

Methods:

- <code title="post /end-users">client.end_users.<a href="./src/conductor/resources/end_users.py">create</a>(\*\*<a href="src/conductor/types/end_user_create_params.py">params</a>) -> <a href="./src/conductor/types/end_user.py">EndUser</a></code>
- <code title="get /end-users/{id}">client.end_users.<a href="./src/conductor/resources/end_users.py">retrieve</a>(id) -> <a href="./src/conductor/types/end_user.py">EndUser</a></code>
- <code title="get /end-users">client.end_users.<a href="./src/conductor/resources/end_users.py">list</a>() -> <a href="./src/conductor/types/end_user_list_response.py">EndUserListResponse</a></code>
- <code title="delete /end-users/{id}">client.end_users.<a href="./src/conductor/resources/end_users.py">delete</a>(id) -> <a href="./src/conductor/types/end_user_delete_response.py">EndUserDeleteResponse</a></code>
- <code title="post /end-users/{id}/passthrough/{integrationSlug}">client.end_users.<a href="./src/conductor/resources/end_users.py">passthrough_integration</a>(integration_slug, \*, id, \*\*<a href="src/conductor/types/end_user_passthrough_integration_params.py">params</a>) -> <a href="./src/conductor/types/end_user_passthrough_integration_response.py">EndUserPassthroughIntegrationResponse</a></code>
- <code title="get /end-users/{id}/ping/{integrationSlug}">client.end_users.<a href="./src/conductor/resources/end_users.py">ping</a>(integration_slug, \*, id) -> <a href="./src/conductor/types/end_user_ping_response.py">EndUserPingResponse</a></code>

# Qbd

## Accounts

Types:

```python
from conductor.types.qbd import Account, AccountListResponse
```

Methods:

- <code title="post /quickbooks-desktop/accounts">client.qbd.accounts.<a href="./src/conductor/resources/qbd/accounts.py">create</a>(\*\*<a href="src/conductor/types/qbd/account_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/account.py">Account</a></code>
- <code title="get /quickbooks-desktop/accounts/{id}">client.qbd.accounts.<a href="./src/conductor/resources/qbd/accounts.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/account.py">Account</a></code>
- <code title="post /quickbooks-desktop/accounts/{id}">client.qbd.accounts.<a href="./src/conductor/resources/qbd/accounts.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/account_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/account.py">Account</a></code>
- <code title="get /quickbooks-desktop/accounts">client.qbd.accounts.<a href="./src/conductor/resources/qbd/accounts.py">list</a>(\*\*<a href="src/conductor/types/qbd/account_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/account_list_response.py">AccountListResponse</a></code>

## BillCheckPayments

Types:

```python
from conductor.types.qbd import BillCheckPayment
```

Methods:

- <code title="post /quickbooks-desktop/bill-check-payments">client.qbd.bill_check_payments.<a href="./src/conductor/resources/qbd/bill_check_payments.py">create</a>(\*\*<a href="src/conductor/types/qbd/bill_check_payment_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/bill_check_payment.py">BillCheckPayment</a></code>
- <code title="get /quickbooks-desktop/bill-check-payments/{id}">client.qbd.bill_check_payments.<a href="./src/conductor/resources/qbd/bill_check_payments.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/bill_check_payment.py">BillCheckPayment</a></code>
- <code title="post /quickbooks-desktop/bill-check-payments/{id}">client.qbd.bill_check_payments.<a href="./src/conductor/resources/qbd/bill_check_payments.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/bill_check_payment_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/bill_check_payment.py">BillCheckPayment</a></code>
- <code title="get /quickbooks-desktop/bill-check-payments">client.qbd.bill_check_payments.<a href="./src/conductor/resources/qbd/bill_check_payments.py">list</a>(\*\*<a href="src/conductor/types/qbd/bill_check_payment_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/bill_check_payment.py">SyncCursorPage[BillCheckPayment]</a></code>

## BillCreditCardPayments

Types:

```python
from conductor.types.qbd import BillCreditCardPayment
```

Methods:

- <code title="post /quickbooks-desktop/bill-credit-card-payments">client.qbd.bill_credit_card_payments.<a href="./src/conductor/resources/qbd/bill_credit_card_payments.py">create</a>(\*\*<a href="src/conductor/types/qbd/bill_credit_card_payment_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/bill_credit_card_payment.py">BillCreditCardPayment</a></code>
- <code title="get /quickbooks-desktop/bill-credit-card-payments/{id}">client.qbd.bill_credit_card_payments.<a href="./src/conductor/resources/qbd/bill_credit_card_payments.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/bill_credit_card_payment.py">BillCreditCardPayment</a></code>
- <code title="get /quickbooks-desktop/bill-credit-card-payments">client.qbd.bill_credit_card_payments.<a href="./src/conductor/resources/qbd/bill_credit_card_payments.py">list</a>(\*\*<a href="src/conductor/types/qbd/bill_credit_card_payment_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/bill_credit_card_payment.py">SyncCursorPage[BillCreditCardPayment]</a></code>

## Bills

Types:

```python
from conductor.types.qbd import Bill
```

Methods:

- <code title="post /quickbooks-desktop/bills">client.qbd.bills.<a href="./src/conductor/resources/qbd/bills.py">create</a>(\*\*<a href="src/conductor/types/qbd/bill_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/bill.py">Bill</a></code>
- <code title="get /quickbooks-desktop/bills/{id}">client.qbd.bills.<a href="./src/conductor/resources/qbd/bills.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/bill.py">Bill</a></code>
- <code title="post /quickbooks-desktop/bills/{id}">client.qbd.bills.<a href="./src/conductor/resources/qbd/bills.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/bill_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/bill.py">Bill</a></code>
- <code title="get /quickbooks-desktop/bills">client.qbd.bills.<a href="./src/conductor/resources/qbd/bills.py">list</a>(\*\*<a href="src/conductor/types/qbd/bill_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/bill.py">SyncCursorPage[Bill]</a></code>

## Checks

Types:

```python
from conductor.types.qbd import Check
```

Methods:

- <code title="post /quickbooks-desktop/checks">client.qbd.checks.<a href="./src/conductor/resources/qbd/checks.py">create</a>(\*\*<a href="src/conductor/types/qbd/check_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/check.py">Check</a></code>
- <code title="get /quickbooks-desktop/checks/{id}">client.qbd.checks.<a href="./src/conductor/resources/qbd/checks.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/check.py">Check</a></code>
- <code title="post /quickbooks-desktop/checks/{id}">client.qbd.checks.<a href="./src/conductor/resources/qbd/checks.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/check_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/check.py">Check</a></code>
- <code title="get /quickbooks-desktop/checks">client.qbd.checks.<a href="./src/conductor/resources/qbd/checks.py">list</a>(\*\*<a href="src/conductor/types/qbd/check_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/check.py">SyncCursorPage[Check]</a></code>

## Classes

Types:

```python
from conductor.types.qbd import Class, ClassListResponse
```

Methods:

- <code title="post /quickbooks-desktop/classes">client.qbd.classes.<a href="./src/conductor/resources/qbd/classes.py">create</a>(\*\*<a href="src/conductor/types/qbd/class_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/class_.py">Class</a></code>
- <code title="get /quickbooks-desktop/classes/{id}">client.qbd.classes.<a href="./src/conductor/resources/qbd/classes.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/class_.py">Class</a></code>
- <code title="post /quickbooks-desktop/classes/{id}">client.qbd.classes.<a href="./src/conductor/resources/qbd/classes.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/class_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/class_.py">Class</a></code>
- <code title="get /quickbooks-desktop/classes">client.qbd.classes.<a href="./src/conductor/resources/qbd/classes.py">list</a>(\*\*<a href="src/conductor/types/qbd/class_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/class_list_response.py">ClassListResponse</a></code>

## CreditCardCharges

Types:

```python
from conductor.types.qbd import CreditCardCharge
```

Methods:

- <code title="post /quickbooks-desktop/credit-card-charges">client.qbd.credit_card_charges.<a href="./src/conductor/resources/qbd/credit_card_charges.py">create</a>(\*\*<a href="src/conductor/types/qbd/credit_card_charge_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/credit_card_charge.py">CreditCardCharge</a></code>
- <code title="get /quickbooks-desktop/credit-card-charges/{id}">client.qbd.credit_card_charges.<a href="./src/conductor/resources/qbd/credit_card_charges.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/credit_card_charge.py">CreditCardCharge</a></code>
- <code title="post /quickbooks-desktop/credit-card-charges/{id}">client.qbd.credit_card_charges.<a href="./src/conductor/resources/qbd/credit_card_charges.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/credit_card_charge_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/credit_card_charge.py">CreditCardCharge</a></code>
- <code title="get /quickbooks-desktop/credit-card-charges">client.qbd.credit_card_charges.<a href="./src/conductor/resources/qbd/credit_card_charges.py">list</a>(\*\*<a href="src/conductor/types/qbd/credit_card_charge_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/credit_card_charge.py">SyncCursorPage[CreditCardCharge]</a></code>

## CreditCardCredits

Types:

```python
from conductor.types.qbd import CreditCardCredit
```

Methods:

- <code title="post /quickbooks-desktop/credit-card-credits">client.qbd.credit_card_credits.<a href="./src/conductor/resources/qbd/credit_card_credits.py">create</a>(\*\*<a href="src/conductor/types/qbd/credit_card_credit_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/credit_card_credit.py">CreditCardCredit</a></code>
- <code title="get /quickbooks-desktop/credit-card-credits/{id}">client.qbd.credit_card_credits.<a href="./src/conductor/resources/qbd/credit_card_credits.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/credit_card_credit.py">CreditCardCredit</a></code>
- <code title="post /quickbooks-desktop/credit-card-credits/{id}">client.qbd.credit_card_credits.<a href="./src/conductor/resources/qbd/credit_card_credits.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/credit_card_credit_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/credit_card_credit.py">CreditCardCredit</a></code>
- <code title="get /quickbooks-desktop/credit-card-credits">client.qbd.credit_card_credits.<a href="./src/conductor/resources/qbd/credit_card_credits.py">list</a>(\*\*<a href="src/conductor/types/qbd/credit_card_credit_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/credit_card_credit.py">SyncCursorPage[CreditCardCredit]</a></code>

## Customers

Types:

```python
from conductor.types.qbd import Customer
```

Methods:

- <code title="post /quickbooks-desktop/customers">client.qbd.customers.<a href="./src/conductor/resources/qbd/customers.py">create</a>(\*\*<a href="src/conductor/types/qbd/customer_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/customer.py">Customer</a></code>
- <code title="get /quickbooks-desktop/customers/{id}">client.qbd.customers.<a href="./src/conductor/resources/qbd/customers.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/customer.py">Customer</a></code>
- <code title="post /quickbooks-desktop/customers/{id}">client.qbd.customers.<a href="./src/conductor/resources/qbd/customers.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/customer_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/customer.py">Customer</a></code>
- <code title="get /quickbooks-desktop/customers">client.qbd.customers.<a href="./src/conductor/resources/qbd/customers.py">list</a>(\*\*<a href="src/conductor/types/qbd/customer_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/customer.py">SyncCursorPage[Customer]</a></code>

## DateDrivenTerms

Types:

```python
from conductor.types.qbd import DateDrivenTerm, DateDrivenTermListResponse
```

Methods:

- <code title="post /quickbooks-desktop/date-driven-terms">client.qbd.date_driven_terms.<a href="./src/conductor/resources/qbd/date_driven_terms.py">create</a>(\*\*<a href="src/conductor/types/qbd/date_driven_term_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/date_driven_term.py">DateDrivenTerm</a></code>
- <code title="get /quickbooks-desktop/date-driven-terms/{id}">client.qbd.date_driven_terms.<a href="./src/conductor/resources/qbd/date_driven_terms.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/date_driven_term.py">DateDrivenTerm</a></code>
- <code title="get /quickbooks-desktop/date-driven-terms">client.qbd.date_driven_terms.<a href="./src/conductor/resources/qbd/date_driven_terms.py">list</a>(\*\*<a href="src/conductor/types/qbd/date_driven_term_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/date_driven_term_list_response.py">DateDrivenTermListResponse</a></code>

## Estimates

Types:

```python
from conductor.types.qbd import Estimate
```

Methods:

- <code title="post /quickbooks-desktop/estimates">client.qbd.estimates.<a href="./src/conductor/resources/qbd/estimates.py">create</a>(\*\*<a href="src/conductor/types/qbd/estimate_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/estimate.py">Estimate</a></code>
- <code title="get /quickbooks-desktop/estimates/{id}">client.qbd.estimates.<a href="./src/conductor/resources/qbd/estimates.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/estimate.py">Estimate</a></code>
- <code title="post /quickbooks-desktop/estimates/{id}">client.qbd.estimates.<a href="./src/conductor/resources/qbd/estimates.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/estimate_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/estimate.py">Estimate</a></code>
- <code title="get /quickbooks-desktop/estimates">client.qbd.estimates.<a href="./src/conductor/resources/qbd/estimates.py">list</a>(\*\*<a href="src/conductor/types/qbd/estimate_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/estimate.py">SyncCursorPage[Estimate]</a></code>

## InventoryAssemblyItems

Types:

```python
from conductor.types.qbd import InventoryAssemblyItem
```

Methods:

- <code title="post /quickbooks-desktop/inventory-assembly-items">client.qbd.inventory_assembly_items.<a href="./src/conductor/resources/qbd/inventory_assembly_items.py">create</a>(\*\*<a href="src/conductor/types/qbd/inventory_assembly_item_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/inventory_assembly_item.py">InventoryAssemblyItem</a></code>
- <code title="get /quickbooks-desktop/inventory-assembly-items/{id}">client.qbd.inventory_assembly_items.<a href="./src/conductor/resources/qbd/inventory_assembly_items.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/inventory_assembly_item.py">InventoryAssemblyItem</a></code>
- <code title="post /quickbooks-desktop/inventory-assembly-items/{id}">client.qbd.inventory_assembly_items.<a href="./src/conductor/resources/qbd/inventory_assembly_items.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/inventory_assembly_item_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/inventory_assembly_item.py">InventoryAssemblyItem</a></code>
- <code title="get /quickbooks-desktop/inventory-assembly-items">client.qbd.inventory_assembly_items.<a href="./src/conductor/resources/qbd/inventory_assembly_items.py">list</a>(\*\*<a href="src/conductor/types/qbd/inventory_assembly_item_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/inventory_assembly_item.py">SyncCursorPage[InventoryAssemblyItem]</a></code>

## InventoryItems

Types:

```python
from conductor.types.qbd import InventoryItem
```

Methods:

- <code title="post /quickbooks-desktop/inventory-items">client.qbd.inventory_items.<a href="./src/conductor/resources/qbd/inventory_items.py">create</a>(\*\*<a href="src/conductor/types/qbd/inventory_item_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/inventory_item.py">InventoryItem</a></code>
- <code title="get /quickbooks-desktop/inventory-items/{id}">client.qbd.inventory_items.<a href="./src/conductor/resources/qbd/inventory_items.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/inventory_item.py">InventoryItem</a></code>
- <code title="post /quickbooks-desktop/inventory-items/{id}">client.qbd.inventory_items.<a href="./src/conductor/resources/qbd/inventory_items.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/inventory_item_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/inventory_item.py">InventoryItem</a></code>
- <code title="get /quickbooks-desktop/inventory-items">client.qbd.inventory_items.<a href="./src/conductor/resources/qbd/inventory_items.py">list</a>(\*\*<a href="src/conductor/types/qbd/inventory_item_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/inventory_item.py">SyncCursorPage[InventoryItem]</a></code>

## InventorySites

Types:

```python
from conductor.types.qbd import InventorySite, InventorySiteListResponse
```

Methods:

- <code title="post /quickbooks-desktop/inventory-sites">client.qbd.inventory_sites.<a href="./src/conductor/resources/qbd/inventory_sites.py">create</a>(\*\*<a href="src/conductor/types/qbd/inventory_site_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/inventory_site.py">InventorySite</a></code>
- <code title="get /quickbooks-desktop/inventory-sites/{id}">client.qbd.inventory_sites.<a href="./src/conductor/resources/qbd/inventory_sites.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/inventory_site.py">InventorySite</a></code>
- <code title="post /quickbooks-desktop/inventory-sites/{id}">client.qbd.inventory_sites.<a href="./src/conductor/resources/qbd/inventory_sites.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/inventory_site_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/inventory_site.py">InventorySite</a></code>
- <code title="get /quickbooks-desktop/inventory-sites">client.qbd.inventory_sites.<a href="./src/conductor/resources/qbd/inventory_sites.py">list</a>(\*\*<a href="src/conductor/types/qbd/inventory_site_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/inventory_site_list_response.py">InventorySiteListResponse</a></code>

## Invoices

Types:

```python
from conductor.types.qbd import Invoice
```

Methods:

- <code title="post /quickbooks-desktop/invoices">client.qbd.invoices.<a href="./src/conductor/resources/qbd/invoices.py">create</a>(\*\*<a href="src/conductor/types/qbd/invoice_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/invoice.py">Invoice</a></code>
- <code title="get /quickbooks-desktop/invoices/{id}">client.qbd.invoices.<a href="./src/conductor/resources/qbd/invoices.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/invoice.py">Invoice</a></code>
- <code title="post /quickbooks-desktop/invoices/{id}">client.qbd.invoices.<a href="./src/conductor/resources/qbd/invoices.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/invoice_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/invoice.py">Invoice</a></code>
- <code title="get /quickbooks-desktop/invoices">client.qbd.invoices.<a href="./src/conductor/resources/qbd/invoices.py">list</a>(\*\*<a href="src/conductor/types/qbd/invoice_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/invoice.py">SyncCursorPage[Invoice]</a></code>

## NonInventoryItems

Types:

```python
from conductor.types.qbd import NonInventoryItem
```

Methods:

- <code title="post /quickbooks-desktop/non-inventory-items">client.qbd.non_inventory_items.<a href="./src/conductor/resources/qbd/non_inventory_items.py">create</a>(\*\*<a href="src/conductor/types/qbd/non_inventory_item_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/non_inventory_item.py">NonInventoryItem</a></code>
- <code title="get /quickbooks-desktop/non-inventory-items/{id}">client.qbd.non_inventory_items.<a href="./src/conductor/resources/qbd/non_inventory_items.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/non_inventory_item.py">NonInventoryItem</a></code>
- <code title="post /quickbooks-desktop/non-inventory-items/{id}">client.qbd.non_inventory_items.<a href="./src/conductor/resources/qbd/non_inventory_items.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/non_inventory_item_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/non_inventory_item.py">NonInventoryItem</a></code>
- <code title="get /quickbooks-desktop/non-inventory-items">client.qbd.non_inventory_items.<a href="./src/conductor/resources/qbd/non_inventory_items.py">list</a>(\*\*<a href="src/conductor/types/qbd/non_inventory_item_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/non_inventory_item.py">SyncCursorPage[NonInventoryItem]</a></code>

## PurchaseOrders

Types:

```python
from conductor.types.qbd import PurchaseOrder
```

Methods:

- <code title="post /quickbooks-desktop/purchase-orders">client.qbd.purchase_orders.<a href="./src/conductor/resources/qbd/purchase_orders.py">create</a>(\*\*<a href="src/conductor/types/qbd/purchase_order_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/purchase_order.py">PurchaseOrder</a></code>
- <code title="get /quickbooks-desktop/purchase-orders/{id}">client.qbd.purchase_orders.<a href="./src/conductor/resources/qbd/purchase_orders.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/purchase_order.py">PurchaseOrder</a></code>
- <code title="post /quickbooks-desktop/purchase-orders/{id}">client.qbd.purchase_orders.<a href="./src/conductor/resources/qbd/purchase_orders.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/purchase_order_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/purchase_order.py">PurchaseOrder</a></code>
- <code title="get /quickbooks-desktop/purchase-orders">client.qbd.purchase_orders.<a href="./src/conductor/resources/qbd/purchase_orders.py">list</a>(\*\*<a href="src/conductor/types/qbd/purchase_order_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/purchase_order.py">SyncCursorPage[PurchaseOrder]</a></code>

## ReceivePayments

Types:

```python
from conductor.types.qbd import ReceivePayment
```

Methods:

- <code title="post /quickbooks-desktop/receive-payments">client.qbd.receive_payments.<a href="./src/conductor/resources/qbd/receive_payments.py">create</a>(\*\*<a href="src/conductor/types/qbd/receive_payment_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/receive_payment.py">ReceivePayment</a></code>
- <code title="get /quickbooks-desktop/receive-payments/{id}">client.qbd.receive_payments.<a href="./src/conductor/resources/qbd/receive_payments.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/receive_payment.py">ReceivePayment</a></code>
- <code title="post /quickbooks-desktop/receive-payments/{id}">client.qbd.receive_payments.<a href="./src/conductor/resources/qbd/receive_payments.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/receive_payment_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/receive_payment.py">ReceivePayment</a></code>
- <code title="get /quickbooks-desktop/receive-payments">client.qbd.receive_payments.<a href="./src/conductor/resources/qbd/receive_payments.py">list</a>(\*\*<a href="src/conductor/types/qbd/receive_payment_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/receive_payment.py">SyncCursorPage[ReceivePayment]</a></code>

## SalesOrders

Types:

```python
from conductor.types.qbd import SalesOrder
```

Methods:

- <code title="post /quickbooks-desktop/sales-orders">client.qbd.sales_orders.<a href="./src/conductor/resources/qbd/sales_orders.py">create</a>(\*\*<a href="src/conductor/types/qbd/sales_order_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/sales_order.py">SalesOrder</a></code>
- <code title="get /quickbooks-desktop/sales-orders/{id}">client.qbd.sales_orders.<a href="./src/conductor/resources/qbd/sales_orders.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/sales_order.py">SalesOrder</a></code>
- <code title="post /quickbooks-desktop/sales-orders/{id}">client.qbd.sales_orders.<a href="./src/conductor/resources/qbd/sales_orders.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/sales_order_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/sales_order.py">SalesOrder</a></code>
- <code title="get /quickbooks-desktop/sales-orders">client.qbd.sales_orders.<a href="./src/conductor/resources/qbd/sales_orders.py">list</a>(\*\*<a href="src/conductor/types/qbd/sales_order_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/sales_order.py">SyncCursorPage[SalesOrder]</a></code>

## SalesReceipts

Types:

```python
from conductor.types.qbd import SalesReceipt
```

Methods:

- <code title="post /quickbooks-desktop/sales-receipts">client.qbd.sales_receipts.<a href="./src/conductor/resources/qbd/sales_receipts.py">create</a>(\*\*<a href="src/conductor/types/qbd/sales_receipt_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/sales_receipt.py">SalesReceipt</a></code>
- <code title="get /quickbooks-desktop/sales-receipts/{id}">client.qbd.sales_receipts.<a href="./src/conductor/resources/qbd/sales_receipts.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/sales_receipt.py">SalesReceipt</a></code>
- <code title="post /quickbooks-desktop/sales-receipts/{id}">client.qbd.sales_receipts.<a href="./src/conductor/resources/qbd/sales_receipts.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/sales_receipt_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/sales_receipt.py">SalesReceipt</a></code>
- <code title="get /quickbooks-desktop/sales-receipts">client.qbd.sales_receipts.<a href="./src/conductor/resources/qbd/sales_receipts.py">list</a>(\*\*<a href="src/conductor/types/qbd/sales_receipt_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/sales_receipt.py">SyncCursorPage[SalesReceipt]</a></code>

## SalesTaxCodes

Types:

```python
from conductor.types.qbd import SalesTaxCode, SalesTaxCodeListResponse
```

Methods:

- <code title="post /quickbooks-desktop/sales-tax-codes">client.qbd.sales_tax_codes.<a href="./src/conductor/resources/qbd/sales_tax_codes.py">create</a>(\*\*<a href="src/conductor/types/qbd/sales_tax_code_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/sales_tax_code.py">SalesTaxCode</a></code>
- <code title="get /quickbooks-desktop/sales-tax-codes/{id}">client.qbd.sales_tax_codes.<a href="./src/conductor/resources/qbd/sales_tax_codes.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/sales_tax_code.py">SalesTaxCode</a></code>
- <code title="post /quickbooks-desktop/sales-tax-codes/{id}">client.qbd.sales_tax_codes.<a href="./src/conductor/resources/qbd/sales_tax_codes.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/sales_tax_code_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/sales_tax_code.py">SalesTaxCode</a></code>
- <code title="get /quickbooks-desktop/sales-tax-codes">client.qbd.sales_tax_codes.<a href="./src/conductor/resources/qbd/sales_tax_codes.py">list</a>(\*\*<a href="src/conductor/types/qbd/sales_tax_code_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/sales_tax_code_list_response.py">SalesTaxCodeListResponse</a></code>

## SalesTaxItems

Types:

```python
from conductor.types.qbd import SalesTaxItem
```

Methods:

- <code title="post /quickbooks-desktop/sales-tax-items">client.qbd.sales_tax_items.<a href="./src/conductor/resources/qbd/sales_tax_items.py">create</a>(\*\*<a href="src/conductor/types/qbd/sales_tax_item_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/sales_tax_item.py">SalesTaxItem</a></code>
- <code title="get /quickbooks-desktop/sales-tax-items/{id}">client.qbd.sales_tax_items.<a href="./src/conductor/resources/qbd/sales_tax_items.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/sales_tax_item.py">SalesTaxItem</a></code>
- <code title="post /quickbooks-desktop/sales-tax-items/{id}">client.qbd.sales_tax_items.<a href="./src/conductor/resources/qbd/sales_tax_items.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/sales_tax_item_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/sales_tax_item.py">SalesTaxItem</a></code>
- <code title="get /quickbooks-desktop/sales-tax-items">client.qbd.sales_tax_items.<a href="./src/conductor/resources/qbd/sales_tax_items.py">list</a>(\*\*<a href="src/conductor/types/qbd/sales_tax_item_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/sales_tax_item.py">SyncCursorPage[SalesTaxItem]</a></code>

## ServiceItems

Types:

```python
from conductor.types.qbd import ServiceItem
```

Methods:

- <code title="post /quickbooks-desktop/service-items">client.qbd.service_items.<a href="./src/conductor/resources/qbd/service_items.py">create</a>(\*\*<a href="src/conductor/types/qbd/service_item_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/service_item.py">ServiceItem</a></code>
- <code title="get /quickbooks-desktop/service-items/{id}">client.qbd.service_items.<a href="./src/conductor/resources/qbd/service_items.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/service_item.py">ServiceItem</a></code>
- <code title="post /quickbooks-desktop/service-items/{id}">client.qbd.service_items.<a href="./src/conductor/resources/qbd/service_items.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/service_item_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/service_item.py">ServiceItem</a></code>
- <code title="get /quickbooks-desktop/service-items">client.qbd.service_items.<a href="./src/conductor/resources/qbd/service_items.py">list</a>(\*\*<a href="src/conductor/types/qbd/service_item_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/service_item.py">SyncCursorPage[ServiceItem]</a></code>

## StandardTerms

Types:

```python
from conductor.types.qbd import StandardTerm, StandardTermListResponse
```

Methods:

- <code title="post /quickbooks-desktop/standard-terms">client.qbd.standard_terms.<a href="./src/conductor/resources/qbd/standard_terms.py">create</a>(\*\*<a href="src/conductor/types/qbd/standard_term_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/standard_term.py">StandardTerm</a></code>
- <code title="get /quickbooks-desktop/standard-terms/{id}">client.qbd.standard_terms.<a href="./src/conductor/resources/qbd/standard_terms.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/standard_term.py">StandardTerm</a></code>
- <code title="get /quickbooks-desktop/standard-terms">client.qbd.standard_terms.<a href="./src/conductor/resources/qbd/standard_terms.py">list</a>(\*\*<a href="src/conductor/types/qbd/standard_term_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/standard_term_list_response.py">StandardTermListResponse</a></code>

## Transfers

Types:

```python
from conductor.types.qbd import Transfer
```

Methods:

- <code title="post /quickbooks-desktop/transfers">client.qbd.transfers.<a href="./src/conductor/resources/qbd/transfers.py">create</a>(\*\*<a href="src/conductor/types/qbd/transfer_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/transfer.py">Transfer</a></code>
- <code title="get /quickbooks-desktop/transfers/{id}">client.qbd.transfers.<a href="./src/conductor/resources/qbd/transfers.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/transfer.py">Transfer</a></code>
- <code title="post /quickbooks-desktop/transfers/{id}">client.qbd.transfers.<a href="./src/conductor/resources/qbd/transfers.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/transfer_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/transfer.py">Transfer</a></code>
- <code title="get /quickbooks-desktop/transfers">client.qbd.transfers.<a href="./src/conductor/resources/qbd/transfers.py">list</a>(\*\*<a href="src/conductor/types/qbd/transfer_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/transfer.py">SyncCursorPage[Transfer]</a></code>

## Vendors

Types:

```python
from conductor.types.qbd import Vendor
```

Methods:

- <code title="post /quickbooks-desktop/vendors">client.qbd.vendors.<a href="./src/conductor/resources/qbd/vendors.py">create</a>(\*\*<a href="src/conductor/types/qbd/vendor_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/vendor.py">Vendor</a></code>
- <code title="get /quickbooks-desktop/vendors/{id}">client.qbd.vendors.<a href="./src/conductor/resources/qbd/vendors.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/vendor.py">Vendor</a></code>
- <code title="post /quickbooks-desktop/vendors/{id}">client.qbd.vendors.<a href="./src/conductor/resources/qbd/vendors.py">update</a>(id, \*\*<a href="src/conductor/types/qbd/vendor_update_params.py">params</a>) -> <a href="./src/conductor/types/qbd/vendor.py">Vendor</a></code>
- <code title="get /quickbooks-desktop/vendors">client.qbd.vendors.<a href="./src/conductor/resources/qbd/vendors.py">list</a>(\*\*<a href="src/conductor/types/qbd/vendor_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/vendor.py">SyncCursorPage[Vendor]</a></code>
