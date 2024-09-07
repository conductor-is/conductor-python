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
    EndUserPingResponse,
    EndUserRequestResponse,
)
```

Methods:

- <code title="post /end-users">client.end_users.<a href="./src/conductor/resources/end_users.py">create</a>(\*\*<a href="src/conductor/types/end_user_create_params.py">params</a>) -> <a href="./src/conductor/types/end_user.py">EndUser</a></code>
- <code title="get /end-users/{id}">client.end_users.<a href="./src/conductor/resources/end_users.py">retrieve</a>(id) -> <a href="./src/conductor/types/end_user.py">EndUser</a></code>
- <code title="get /end-users">client.end_users.<a href="./src/conductor/resources/end_users.py">list</a>() -> <a href="./src/conductor/types/end_user_list_response.py">EndUserListResponse</a></code>
- <code title="get /end-users/{id}/ping/{integrationSlug}">client.end_users.<a href="./src/conductor/resources/end_users.py">ping</a>(integration_slug, \*, id) -> <a href="./src/conductor/types/end_user_ping_response.py">EndUserPingResponse</a></code>
- <code title="post /end-users/{id}/request/{integrationSlug}">client.end_users.<a href="./src/conductor/resources/end_users.py">request</a>(integration_slug, \*, id, \*\*<a href="src/conductor/types/end_user_request_params.py">params</a>) -> <a href="./src/conductor/types/end_user_request_response.py">object</a></code>

# IntegrationConnections

Types:

```python
from conductor.types import IntegrationConnection, IntegrationConnectionListResponse
```

Methods:

- <code title="get /integration-connections/{id}">client.integration_connections.<a href="./src/conductor/resources/integration_connections.py">retrieve</a>(id) -> <a href="./src/conductor/types/integration_connection.py">IntegrationConnection</a></code>
- <code title="get /integration-connections">client.integration_connections.<a href="./src/conductor/resources/integration_connections.py">list</a>() -> <a href="./src/conductor/types/integration_connection_list_response.py">IntegrationConnectionListResponse</a></code>

# Qbd

## Accounts

Types:

```python
from conductor.types.qbd import QbdAccount, AccountListResponse
```

Methods:

- <code title="post /quickbooks-desktop/accounts">client.qbd.accounts.<a href="./src/conductor/resources/qbd/accounts.py">create</a>(\*\*<a href="src/conductor/types/qbd/account_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/qbd_account.py">QbdAccount</a></code>
- <code title="get /quickbooks-desktop/accounts/{id}">client.qbd.accounts.<a href="./src/conductor/resources/qbd/accounts.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/qbd_account.py">QbdAccount</a></code>
- <code title="get /quickbooks-desktop/accounts">client.qbd.accounts.<a href="./src/conductor/resources/qbd/accounts.py">list</a>(\*\*<a href="src/conductor/types/qbd/account_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/account_list_response.py">AccountListResponse</a></code>

## Bills

Types:

```python
from conductor.types.qbd import QbdBill
```

Methods:

- <code title="post /quickbooks-desktop/bills">client.qbd.bills.<a href="./src/conductor/resources/qbd/bills.py">create</a>(\*\*<a href="src/conductor/types/qbd/bill_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/qbd_bill.py">QbdBill</a></code>
- <code title="get /quickbooks-desktop/bills/{id}">client.qbd.bills.<a href="./src/conductor/resources/qbd/bills.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/qbd_bill.py">QbdBill</a></code>
- <code title="get /quickbooks-desktop/bills">client.qbd.bills.<a href="./src/conductor/resources/qbd/bills.py">list</a>(\*\*<a href="src/conductor/types/qbd/bill_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/qbd_bill.py">SyncMyCursorPage[QbdBill]</a></code>

## Classes

Types:

```python
from conductor.types.qbd import QbdClass, ClassListResponse
```

Methods:

- <code title="post /quickbooks-desktop/classes">client.qbd.classes.<a href="./src/conductor/resources/qbd/classes.py">create</a>(\*\*<a href="src/conductor/types/qbd/class_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/qbd_class.py">QbdClass</a></code>
- <code title="get /quickbooks-desktop/classes/{id}">client.qbd.classes.<a href="./src/conductor/resources/qbd/classes.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/qbd_class.py">QbdClass</a></code>
- <code title="get /quickbooks-desktop/classes">client.qbd.classes.<a href="./src/conductor/resources/qbd/classes.py">list</a>(\*\*<a href="src/conductor/types/qbd/class_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/class_list_response.py">ClassListResponse</a></code>

## CreditCardCharges

Types:

```python
from conductor.types.qbd import QbdCreditCardCharge
```

Methods:

- <code title="post /quickbooks-desktop/credit-card-charges">client.qbd.credit_card_charges.<a href="./src/conductor/resources/qbd/credit_card_charges.py">create</a>(\*\*<a href="src/conductor/types/qbd/credit_card_charge_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/qbd_credit_card_charge.py">QbdCreditCardCharge</a></code>
- <code title="get /quickbooks-desktop/credit-card-charges/{id}">client.qbd.credit_card_charges.<a href="./src/conductor/resources/qbd/credit_card_charges.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/qbd_credit_card_charge.py">QbdCreditCardCharge</a></code>
- <code title="get /quickbooks-desktop/credit-card-charges">client.qbd.credit_card_charges.<a href="./src/conductor/resources/qbd/credit_card_charges.py">list</a>(\*\*<a href="src/conductor/types/qbd/credit_card_charge_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/qbd_credit_card_charge.py">SyncMyCursorPage[QbdCreditCardCharge]</a></code>

## Customers

Types:

```python
from conductor.types.qbd import QbdCustomer
```

Methods:

- <code title="post /quickbooks-desktop/customers">client.qbd.customers.<a href="./src/conductor/resources/qbd/customers.py">create</a>(\*\*<a href="src/conductor/types/qbd/customer_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/qbd_customer.py">QbdCustomer</a></code>
- <code title="get /quickbooks-desktop/customers/{id}">client.qbd.customers.<a href="./src/conductor/resources/qbd/customers.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/qbd_customer.py">QbdCustomer</a></code>
- <code title="get /quickbooks-desktop/customers">client.qbd.customers.<a href="./src/conductor/resources/qbd/customers.py">list</a>(\*\*<a href="src/conductor/types/qbd/customer_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/qbd_customer.py">SyncMyCursorPage[QbdCustomer]</a></code>

## Invoices

Types:

```python
from conductor.types.qbd import QbdInvoice
```

Methods:

- <code title="post /quickbooks-desktop/invoices">client.qbd.invoices.<a href="./src/conductor/resources/qbd/invoices.py">create</a>(\*\*<a href="src/conductor/types/qbd/invoice_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/qbd_invoice.py">QbdInvoice</a></code>
- <code title="get /quickbooks-desktop/invoices/{id}">client.qbd.invoices.<a href="./src/conductor/resources/qbd/invoices.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/qbd_invoice.py">QbdInvoice</a></code>
- <code title="get /quickbooks-desktop/invoices">client.qbd.invoices.<a href="./src/conductor/resources/qbd/invoices.py">list</a>(\*\*<a href="src/conductor/types/qbd/invoice_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/qbd_invoice.py">SyncMyCursorPage[QbdInvoice]</a></code>

## StandardTerms

Types:

```python
from conductor.types.qbd import QbdStandardTerm, StandardTermListResponse
```

Methods:

- <code title="get /quickbooks-desktop/standard-terms/{id}">client.qbd.standard_terms.<a href="./src/conductor/resources/qbd/standard_terms.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/qbd_standard_term.py">QbdStandardTerm</a></code>
- <code title="get /quickbooks-desktop/standard-terms">client.qbd.standard_terms.<a href="./src/conductor/resources/qbd/standard_terms.py">list</a>(\*\*<a href="src/conductor/types/qbd/standard_term_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/standard_term_list_response.py">StandardTermListResponse</a></code>

## Vendors

Types:

```python
from conductor.types.qbd import QbdVendor
```

Methods:

- <code title="post /quickbooks-desktop/vendors">client.qbd.vendors.<a href="./src/conductor/resources/qbd/vendors.py">create</a>(\*\*<a href="src/conductor/types/qbd/vendor_create_params.py">params</a>) -> <a href="./src/conductor/types/qbd/qbd_vendor.py">QbdVendor</a></code>
- <code title="get /quickbooks-desktop/vendors/{id}">client.qbd.vendors.<a href="./src/conductor/resources/qbd/vendors.py">retrieve</a>(id) -> <a href="./src/conductor/types/qbd/qbd_vendor.py">QbdVendor</a></code>
- <code title="get /quickbooks-desktop/vendors">client.qbd.vendors.<a href="./src/conductor/resources/qbd/vendors.py">list</a>(\*\*<a href="src/conductor/types/qbd/vendor_list_params.py">params</a>) -> <a href="./src/conductor/types/qbd/qbd_vendor.py">SyncMyCursorPage[QbdVendor]</a></code>
